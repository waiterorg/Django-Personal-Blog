from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter


# Create your models here.

class Article(models.Model):
    
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
    )

    title = models.CharField(max_length = 150, verbose_name='عنوان')
    slug = models.SlugField(max_length= 150, unique = True , verbose_name='ادرس لینک')
    description = models.TextField(verbose_name='توضیحات')
    thumpnail = models.ImageField(upload_to = 'blog-images',verbose_name='تصویر')
    publish = models.DateTimeField(default = timezone.now,verbose_name='منتشر شده')
    created = models.DateTimeField(auto_now_add=True,verbose_name='ساخته شده')
    updated = models.DateTimeField(auto_now=True,verbose_name='بروز رسانی شده')
    status = models.CharField(max_length= 1,choices=STATUS_CHOICES,verbose_name='وضعیت')

    class Meta:
         verbose_name = 'مقاله'
         verbose_name_plural = 'مقالات'
    
    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    

    