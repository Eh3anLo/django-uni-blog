from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation 
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import uri_to_iri

# import uuid
from django_editorjs_fields import EditorJsJSONField
from hitcount.models import HitCountMixin, HitCount
from taggit.managers import TaggableManager
from accounts.models import CustomUser
# Create your models here.

class Article(models.Model):
    status_choices = {
        'منتشر شده' : 'منتشر شده',
        'پیش نویس' : 'پیش نویس'
    }
    # id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=100 , db_collation='utf8_persian_ci' , verbose_name="عنوان")
    description = models.TextField(blank=True,null=True, verbose_name="مقدمه")
    img = models.ImageField(upload_to ='uploads/% Y/% m/% d/',null=True , blank=True, verbose_name="تصویر")
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE, verbose_name="نویسنده")
    body = EditorJsJSONField()
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    date_last_modified = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    status = models.CharField(max_length=50 ,choices=status_choices, verbose_name="وضعیت")
    slug = models.SlugField(verbose_name="آدرس"  , allow_unicode=True  , db_collation='utf8_persian_ci')
    views = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    upvotes = models.ManyToManyField(CustomUser , related_name="upvotes" , blank=True , verbose_name="تعداد پسند ها")
    tags = TaggableManager(_("Tags") , blank=True)

    views.short_description = "بازدیدها"
    body.short_description = "محتوا"
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
    
    class Meta:
        verbose_name = "نوشته"
        verbose_name_plural = "مقالات"
    
    

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE , verbose_name="نوشته")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE ,verbose_name="نویسنده")
    content = models.TextField(verbose_name="متن کامنت")
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="تاریخ ثبت")

    def __str__(self):
        return f'کامنت ثبت شده از {self.author} در نوشته {self.article}'
    
    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "نظرها"
