from django.shortcuts import render , get_object_or_404
from .models import UserProfile
from accounts.models import CustomUser
from articles.models import Article
# Create your views here.
def user_profile_view(request , username):
    author = get_object_or_404(CustomUser , username = username)
    user_profile = get_object_or_404(UserProfile , user = author)
    if author:
        if request.user.id == author.id:
            user_articles = Article.objects.filter(author = author)
        else:
            user_articles = Article.objects.filter(author = author , status='منتشر شده')
    return render(request , 'profiles/profile.html' , {"user_profile" : user_profile , "articles" : user_articles , 'author_id' : author.id})
