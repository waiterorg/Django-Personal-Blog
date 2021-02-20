from django.shortcuts import render , get_object_or_404
from .models import Article
from django.views.generic.detail import DetailView
# Create your views here.

def home(request):
    articles = Article.objects.filter(status="p")

    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)

class ArticleDetail(DetailView):
    
    model = Article

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = Article.objects.filter(status = 'p') 
        return get_object_or_404(article , slug=slug)