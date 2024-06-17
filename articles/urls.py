from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/<slug:slug>/' , views.ArticleDetailView.as_view() , name="article_detail"),
    path('create/' , views.ArticleCreateView.as_view(), name="create_article"),
    path('<int:id>/<slug:slug>/update/' , views.ArticleUpdateView.as_view() , name='update_article'),
    path('<int:id>/delete' , views.ArticleDeleteView.as_view() , name="article_delete")
    # path('<uuid:id>/<slug:slug>' , views.article_detail_view_by_id , name='detial_view_id')
]