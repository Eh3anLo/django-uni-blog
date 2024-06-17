from django import forms
from django_editorjs_fields import EditorJsWidget
from articles.models import Article

class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title' , 'img' , 'description' , 'status' , 'body']
        exclude = []
        widgets = {
            'body': EditorJsWidget(config={'minHeight': 100}),
            'body': EditorJsWidget(plugins=["@editorjs/image", "@editorjs/header"])
        }

    def set_author(self , user):
        Article.author = user
