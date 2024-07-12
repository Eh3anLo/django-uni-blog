from django.contrib import admin
from .models import Article , Comment
# Register your models here.
class CommentAdmin(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'author' , 'slug' , 'status')
    search_fields = ('title', 'content',)
    list_filter = ('tags',)
    list_editable = ('status' , 'author')
    inlines = [CommentAdmin]
    # prepopulated_fields = {"slug": ("title",)}
admin.site.register(Article , ArticleAdmin)