from django.contrib import admin
from .models import Article , Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'position', 'title', 'slug', 'parent', 'status',)
    list_filter = ('status',)
    search_field = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','jpublish', 'jupdated', 'status',  'category_to_str')
    list_filter = ('publish', 'status')
    search_field = ('title', 'description')
    ordering = ['-status','-publish']

    def category_to_str(self, obj):
        return " ,".join([category.title for category in obj.category.get_active_category()])

    category_to_str.short_description='دسته بندی'

admin.site.register(Article, ArticleAdmin)
