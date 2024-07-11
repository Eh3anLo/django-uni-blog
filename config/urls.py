"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from django.views.generic import TemplateView

from . import views
from articles.views import ArticlesListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home_page , name='home'),
    path('accounts/' , include('accounts.urls')),
    path('articles/' , include('articles.urls')),
    path('authors/' , include('profiles.urls')),
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)