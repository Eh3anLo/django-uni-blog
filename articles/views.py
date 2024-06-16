from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_editorjs_fields import EditorJsWidget
from hitcount.views import HitCountDetailView
from .forms import ArticleCreationForm
from .models import Article
# Create your views here.
class ArticleDetailView(HitCountDetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    count_hit = True

class ArticlesListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'

    def get_queryset(self):
        return Article.objects.filter(status = 'pub')

class ArticleCreationView(LoginRequiredMixin , CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articles/article_create.html'
    success_url = reverse_lazy('home')
    


# def article_detail_view_by_id(request , id , slug):
#     article = Article.objects.get(pk = id , slug=slug)
#     return render(request , 'articles/article_detail.html' , { 'article' : article})