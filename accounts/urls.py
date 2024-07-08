from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import CustomAuthenticationForm
from . import views
urlpatterns = [
    path("login/" ,views.SendOTPView.as_view() , name="login" ),
    path('signup/' ,views.SendOTPView.as_view() , name='signup'),
    path('register/' ,views.ValidateOTPView.as_view() , name='validate_otp'),
    path('logout/' , auth_views.LogoutView.as_view() , name="signout")
]