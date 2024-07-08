from django.urls import path , re_path , include
from . import views
urlpatterns = [
    path('' , views.ArticlesListView.as_view() , name="article_list"),
    path('<int:id>/<str:slug>' , views.ArticleDetailView.as_view() , name="article_detail"),
    path('create/' , views.ArticleCreateView.as_view(), name="create_article"),
    path('<int:id>/<str:slug>/update/' , views.ArticleUpdateView.as_view() , name='update_article'),
    path('<int:id>/delete' , views.ArticleDeleteView.as_view() , name="article_delete"),
    path('<int:id>/<str:slug>/upvote' , views.article_upvotes_view , name="upvote_article"),
    path('editorjs/', include('django_editorjs_fields.urls')),
    # path('<uuid:id>/<slug:slug>' , views.article_detail_view_by_id , name='detial_view_id')
]