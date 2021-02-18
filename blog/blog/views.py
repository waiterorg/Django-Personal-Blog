from django.shortcuts import render
from .models import Article
# Create your views here.

def home(request):
    articles = Article.objects.filter(status="p")

    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)