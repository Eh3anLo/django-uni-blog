from django.shortcuts import redirect, render , get_object_or_404 
from django.contrib.auth.decorators import login_required


from .models import UserProfile
from .forms import ProfileUpdateForm
from accounts.models import CustomUser
from accounts.forms import CustomUserUpdateForm
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

@login_required
def update_user_profile(request):
    print("im heare")
    user = request.user
    try:
        profile = get_object_or_404(UserProfile , user=user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, request.FILES,  instance=user)
        profile_form = ProfileUpdateForm(request.POST,instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile' , username=user.username )  # Redirect to a success page or profile page
    else:
        user_form = CustomUserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'profiles/profile_setting.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
