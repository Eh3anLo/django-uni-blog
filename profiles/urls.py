from django.urls import path
from . import views
urlpatterns = [
    path('<str:username>/profile' , views.user_profile_view , name='user_profile'),
]