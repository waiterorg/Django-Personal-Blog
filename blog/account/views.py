from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixnis import FieldsMixin , FormValidMixin , AuthorAccessMixin, SuperUserAccessMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.models import Article

# Create your views here.
class ArticleList(LoginRequiredMixin, ListView):
	template_name = "registration/home.html"

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all()
		else:
			return Article.objects.filter(author=self.request.user)



class ArticleCreate(LoginRequiredMixin, FieldsMixin, FormValidMixin, CreateView):
	model = Article
	template_name = "registration/article-create-update.html"

class ArticleUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
	model = Article
	template_name = "registration/article-create-update.html"

class ArticleDelete(SuperUserAccessMixin, DeleteView):
	model = Article
	success_url = reverse_lazy('account:home')
	template_name = "registration/article-confirm-delete.html"