from django.shortcuts import render , get_object_or_404
from .models import UserProfile
from accounts.models import CustomUser
# Create your views here.
def user_profile_view(request , username):
    user_id = get_object_or_404(CustomUser , username = username)
    user_profile = get_object_or_404(UserProfile , user = user_id)
    return render(request , 'profiles/profile.html' , {"user_profile" : user_profile})
