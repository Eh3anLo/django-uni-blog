from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/<slug:slug>' , views.article_detail_view , name='article_detail'),
    path('create/' , views.ArticleCreationView.as_view(), name="create_article"),
    # path('<uuid:id>/<slug:slug>' , views.article_detail_view_by_id , name='detial_view_id')
]