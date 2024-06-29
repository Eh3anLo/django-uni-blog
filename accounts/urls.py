from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import CustomAuthenticationForm
from . import views
urlpatterns = [
    path("login/" , auth_views.LoginView.as_view(authentication_form = CustomAuthenticationForm) , name="login" ),
    path('signup/' ,views.SignUpView.as_view() , name='signup')
]