from django import forms
from django_editorjs_fields import EditorJsWidget
from articles.models import Article

class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title' , 'img' , 'description' , 'status' , 'body']
        exclude = []


    def set_author(self , user):
        Article.author = user
