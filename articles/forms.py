from django import forms
from django_editorjs_fields import EditorJsWidget
from articles.models import Article , Comment

class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title' , 'img' , 'description' , 'status' , 'body' , 'tags']
        labels = {
            'tags' : "برچسب ها"
        }
        widgets = {
            'title' : forms.TextInput(attrs={"placeholder" : "عنوان ..."}),
            'description' : forms.Textarea(attrs={"placeholder" : "توضیحات..."}),
            'tags' : forms.TextInput(attrs={"placeholder" : "برچسب ها"}),
            'img' : forms.FileInput(attrs={'class' : "custom-file-upload"}),
            'status' : forms.Select(attrs={"title" : "وضعیت"})
        }
        help_texts = {
            "tags" : "با ( ، ) میتوانید تا ۵ برچسب وارد کنید"
        }
        exclude = []


    def set_author(self , user):
        Article.author = user
            
    def __init__(self, *args, **kwargs):
        super(ArticleCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':f' فیلد ({field.label})  الزامی ست.'}
    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if len(tags) > 5:
            raise forms.ValidationError("You can only add up to 5 tags.")
        return tags

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title' , 'img' , 'description' , 'status' , 'body' , 'tags']
        labels = {
            'tags' : "برچسب ها"
        }
        widgets = {
            'title' : forms.TextInput(attrs={"placeholder" : "عنوان ..."}),
            'description' : forms.Textarea(attrs={"placeholder" : "توضیحات..."}),
            'tags' : forms.TextInput(attrs={"placeholder" : "برچسب ها"}),
            'img' : forms.FileInput(attrs={'class' : "custom-file-upload"}),
            'status' : forms.Select(attrs={"title" : "وضعیت"})
        }
        help_texts = {
            "tags" : "با ( ، ) میتوانید تا ۵ برچسب وارد کنید"
        }
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super(ArticleUpdateForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':f' فیلد ({field.label})  الزامی ست.'}

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if len(tags) > 5:
            raise forms.ValidationError("You can only add up to 5 tags.")
        return tags
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'افزودن کامنت ... '}),
        }

class ArticleSearchForm(forms.Form):
    query = forms.CharField(label='جست و جو', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'جست و جو ...'}))