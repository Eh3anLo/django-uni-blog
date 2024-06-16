from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation 
from django.utils.text import slugify
# import uuid
from django_editorjs_fields import EditorJsJSONField
from hitcount.models import HitCountMixin, HitCount
# Create your models here.

class Article(models.Model):
    status_choices = {
        'pub' : 'published',
        'crf' : 'crafted'
    }
    # id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to='media', null=True , blank=True)
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)
    body = EditorJsJSONField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50 ,choices=status_choices)
    slug = models.SlugField(blank=True)
    views = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    upvote = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title + '-' + str(self.id).split('-')[0] )
        self.slug = slugify(self.title.lower())
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"id": self.pk , "slug" : self.slug})
    
