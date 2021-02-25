from django.shortcuts import render , get_object_or_404
from .models import Article , Category
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.get_published_article()
    paginate_by = 2


class ArticleDetail(DetailView):
    
    model = Article

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = Article.objects.filter(status = 'p') 
        return get_object_or_404(article , slug=slug)




class CategoryView(DetailView):
    
    model = Category

    def get_object(self):
        slug = self.kwargs.get('slug')
        category = Category.objects.get_active_category()
        return get_object_or_404(category , slug=slug)