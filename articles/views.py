from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_editorjs_fields import EditorJsWidget
from .forms import ArticleCreationForm
from .models import Article
# Create your views here.
def article_detail_view(request , id , slug):
    article = Article.objects.get(pk = id ,slug = slug)
    return render(request , 'articles/article_detail.html' , { 'article' : article})


class ArticlesListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'

class ArticleCreationView(LoginRequiredMixin , CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articles/article_create.html'
    success_url = reverse_lazy('home')
    


# def article_detail_view_by_id(request , id , slug):
#     article = Article.objects.get(pk = id , slug=slug)
#     return render(request , 'articles/article_detail.html' , { 'article' : article})