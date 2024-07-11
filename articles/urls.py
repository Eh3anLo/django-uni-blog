from django.urls import path , re_path , include
from . import views
urlpatterns = [
    path('' , views.ArticlesListView.as_view() , name="article_list"),
    path('<int:id>/<str:slug>/' , views.ArticleDetailView.as_view() , name="article_detail"),
    path('create/' , views.ArticleCreateView.as_view(), name="create_article"),
    path('<int:id>/<str:slug>/update/' , views.ArticleUpdateView.as_view() , name='update_article'),
    path('delete/<int:id>/' , views.ArticleDeleteView.as_view() , name="article_delete"),
    path('<int:id>/<str:slug>/upvote/' , views.article_upvotes_view , name="upvote_article"),
    re_path(r'tags/(?P<slug>[^/]+)/?', views.articles_by_tag, name='articles_by_tag'),
    # path('<uuid:id>/<slug:slug>' , views.article_detail_view_by_id , name='detial_view_id')
]