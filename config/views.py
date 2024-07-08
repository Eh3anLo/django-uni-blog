from django.shortcuts import redirect , render
from django.views.generic import View

def home_page(request):
    user_authenticate = request.user.is_authenticated
    if user_authenticate:
        return redirect('article_list')
    return render(request , 'home.html')