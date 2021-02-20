from django.urls import path
from .views import home , ArticleDetail

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="articledetail"),

]