from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect , HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.encoding import uri_to_iri


from hitcount.views import HitCountDetailView
from taggit.models import Tag

from .forms import ArticleCreationForm , ArticleUpdateForm
from .models import Article
from profiles.models import UserProfile

# Create your views here.
class ArticleDetailView(LoginRequiredMixin , HitCountDetailView , DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    count_hit = True

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        upvotes_connected = get_object_or_404(Article, id=self.kwargs['id'])
        author_articles = Article.objects.filter(author=upvotes_connected.author , status="منتشر شده")
        upvoted = False
        if upvotes_connected.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        ctx['author_articles'] = author_articles
        print(author_articles)
        print(upvotes_connected)
        ctx['number_of_upvotes'] = upvotes_connected.number_of_upvotes()
        ctx['article_is_upvoted'] = upvoted
        return ctx
    
    def get_object(self):
        return get_object_or_404(Article, id = self.kwargs['id'] , slug=self.kwargs['slug'])


class ArticlesListView(LoginRequiredMixin , ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'

    def get_queryset(self):
        return Article.objects.filter(status = 'منتشر شده')

def articles_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=uri_to_iri(slug))
    articles = Article.objects.filter(tags=tag)
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