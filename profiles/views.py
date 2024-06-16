from django.shortcuts import render , get_object_or_404
from .models import UserProfile
from accounts.models import CustomUser
from articles.models import Article
# Create your views here.
def user_profile_view(request , username):
    user_id = get_object_or_404(CustomUser , username = username)
    user_profile = get_object_or_404(UserProfile , user = user_id)
    if user_profile:
        user_articles = Article.objects.filter(author = user_id)
    return render(request , 'profiles/profile.html' , {"user_profile" : user_profile , "articles" : user_articles})
