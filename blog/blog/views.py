from django.shortcuts import render , get_object_or_404
from .models import Article , Category
from account.models import User
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from account.mixins import AuthorAccessMixin
# Create your views here.

class ArticleListView(ListView):
    queryset = Article.objects.get_published_article()
    paginate_by = 2


class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = Article.objects.get_published_article()
        return get_object_or_404(article , slug=slug)

class ArticlePreview(AuthorAccessMixin, DetailView):

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article , pk=pk)


class CategoryList(ListView):
    paginate_by = 2
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.get_active_category() , slug=slug)
        return category.articles.get_published_article()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
	paginate_by = 2
	template_name = 'blog/author_list.html'

	def get_queryset(self):
		global author
		username = self.kwargs.get('username')
		author = get_object_or_404(User, username=username)
		return author.article.get_published_article()
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context

