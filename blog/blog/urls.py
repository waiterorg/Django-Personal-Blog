from django.urls import path
from .views import ArticleListView, ArticleDetail , CategoryList , AuthorList, ArticlePreview

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="ArticleListView"),
    path('page/<int:page>', ArticleListView.as_view(), name="ArticleListView"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="articledetail"),
    path('category/<slug:slug>', CategoryList.as_view(), name="CategoryView"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="CategoryView"),
    path('preview/<int:pk>', ArticlePreview.as_view(), name="preview"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),

]