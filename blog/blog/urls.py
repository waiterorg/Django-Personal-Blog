from django.urls import path
from .views import ArticleListView, ArticleDetail , CategoryView

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="ArticleListView"),
    path('page/<int:page>', ArticleListView.as_view(), name="ArticleListView"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="articledetail"),
    path('category/<slug:slug>', CategoryView.as_view(), name="CategoryView"),

]