from django.contrib import admin
from .models import Article , Category
# Register your models here.
def make_published(self,request,queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = 'منتشر شد'
    else : 
        message_bit = 'منتشر شدند'
    self.message_user(request,'{} مقاله {}'.format(rows_updated, message_bit))

make_published.short_description = 'انتشار مقالات انتخاب شده'


def make_draft(self,request,queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = 'پیش نویس شد'
    else : 
        message_bit = 'پیش نویس شدند'
    self.message_user(request,'{} مقاله {}'.format(rows_updated, message_bit))

make_draft.short_description = 'پیش نویس مقالات انتخاب شده'



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
    actions = [make_draft, make_published]

    def category_to_str(self, obj):
        return " ,".join([category.title for category in obj.category.get_active_category()])

    category_to_str.short_description='دسته بندی'

admin.site.register(Article, ArticleAdmin)
