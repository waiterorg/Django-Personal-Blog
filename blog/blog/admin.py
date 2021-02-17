from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created', 'updated', 'status')
    list_filter = ('created', 'publish')
    search_field = ('title', 'description')



admin.site.register(Article, ArticleAdmin)
