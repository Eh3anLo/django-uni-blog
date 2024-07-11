from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'author' , 'slug' , 'status')
    search_fields = ('title', 'content',)
    list_filter = ('tags',)
    list_editable = ('status' , 'author')
    # prepopulated_fields = {"slug": ("title",)}
admin.site.register(Article , ArticleAdmin)