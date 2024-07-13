from django.db.models.base import Model as Model
from django.db.models import Count
from django.http import HttpResponseRedirect , HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView
from django.views.generic.edit import FormMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.utils.encoding import uri_to_iri


from hitcount.views import HitCountDetailView
from hitcount.models import Hit , HitCount
from taggit.models import Tag

from .forms import ArticleCreationForm , ArticleUpdateForm , CommentForm
from .models import Article
from profiles.models import UserProfile

# Create your views here.
class ArticleDetailView(LoginRequiredMixin ,FormMixin, HitCountDetailView , DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    form_class = CommentForm
    count_hit = True

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        upvotes_connected = get_object_or_404(Article, id=self.kwargs['id'])
        author_articles = Article.objects.filter(author=upvotes_connected.author , status="منتشر شده").order_by("-date_created")[:5]
        upvoted = False
        if upvotes_connected.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        ctx['author_articles'] = author_articles
        ctx['comments'] = self.object.comments.all()
        ctx['comment_form'] = self.get_form()
        ctx['number_of_upvotes'] = upvotes_connected.number_of_upvotes()
        ctx['article_is_upvoted'] = upvoted
        return ctx
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return redirect('article_detail', id=self.object.pk , slug=self.object.slug)
    
    def get_object(self):
        return get_object_or_404(Article, id = self.kwargs['id'] , slug=self.kwargs['slug'])


class ArticlesListView(LoginRequiredMixin , ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Article.objects.filter(status = 'منتشر شده').order_by("-date_created")
        query = self.request.GET.get('q')
        filter_type = self.request.GET.get('filter')
        if query:
            queryset = queryset.filter(
                status = 'منتشر شده',
                title__icontains=query,
            )
        
        if filter_type == 'latest':
            queryset = queryset.order_by('-date_last_modified')
        elif filter_type == 'most_viewed':
            queryset = queryset.order_by('views')
        elif filter_type == 'trending':
            queryset = queryset.annotate(count=Count('upvotes')).order_by('-count')
        elif filter_type == 'liked_by_user':
            queryset = queryset.filter(upvotes=self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hits = Hit.objects.filter(user=self.request.user)
        hit_counts = HitCount.objects.filter(hit__in=hits)
        context['recent_articles'] = Article.objects.filter(status="منتشر شده" , views__in = hit_counts)[:5]
        context['filter'] = self.request.GET.get('filter', '')
        return context

def articles_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=uri_to_iri(slug))
    articles = Article.objects.filter(status="منتشر شده",tags=tag)
    return render(request, 'articles/article_list.html', {'tag': tag, 'articles': articles})

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articles/article_create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save
        return super().form_valid(form)
    

class ArticleUpdateView(LoginRequiredMixin , UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'articles/article_update.html'

    def get_object(self, queryset=None):
        """
        Check the logged in user is the owner of the object or 404
        """
        obj = super(ArticleUpdateView, self).get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj

class ArticleDeleteView(LoginRequiredMixin , DeleteView):
    model = Article
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        """
        Check the logged in user is the owner of the object or 403
        """
        obj = super(ArticleDeleteView, self).get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj
    
def article_upvotes_view(request , id , slug):    
    article = get_object_or_404(Article, pk=id , slug=slug)
    if article.upvotes.filter(id=request.user.id).exists():
        article.upvotes.remove(request.user.id)
    else:
        article.upvotes.add(request.user.id)

    # return HttpResponseRedirect(reverse('article_detail', args=[id , slug]))   
    return JsonResponse({'upvote' : article.number_of_upvotes()})