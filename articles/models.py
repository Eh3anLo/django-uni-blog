from django.db import models
from django_editorjs_fields import EditorJsJSONField
from django.utils.text import slugify
import uuid
# Create your models here.

class Article(models.Model):
    status_choices = {
        'pub' : 'published',
        'crf' : 'crafted'
    }
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)
    body = EditorJsJSONField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50 ,choices=status_choices)
    slug = models.SlugField()
    views = models.IntegerField()
    upvote = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
