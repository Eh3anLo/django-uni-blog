from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation 
from django.utils.text import slugify
from django.utils.encoding import uri_to_iri

# import uuid
from django_editorjs_fields import EditorJsJSONField
from hitcount.models import HitCountMixin, HitCount

from accounts.models import CustomUser
# Create your models here.

class Article(models.Model):
    status_choices = {
        'pub' : 'published',
        'crf' : 'crafted'
    }
    # id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=100 , db_collation='utf8_persian_ci')
    description = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to='media', null=True , blank=True)
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)
    body = EditorJsJSONField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50 ,choices=status_choices)
    slug = models.SlugField(verbose_name="آدرس"  , allow_unicode=True  , db_collation='utf8_persian_ci')
    views = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    upvotes = models.ManyToManyField(CustomUser , related_name="upvotes" , blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title + '-' + str(self.id).split('-')[0] )
        if len(self.title) > 50:
            self.slug = slugify(self.title[:50].lower() , allow_unicode=True)
        else:
            self.slug  = slugify(self.title.lower() , allow_unicode=True)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"id": self.pk , "slug" : uri_to_iri(self.slug)})
    
    def number_of_upvotes(self):
        return self.upvotes.count()
