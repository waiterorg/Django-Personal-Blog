from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='ادرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(default=0, verbose_name='پوزیشن')

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=['position']

    def __str__(self):
        return self.title




class Article(models.Model):
    
    STATUS_CHOICES = (
        ('d','چک نویس'),
        ('p','منتشر شده'),
    )

    title = models.CharField(max_length = 150, verbose_name='عنوان')
    slug = models.SlugField(max_length= 150, unique = True , verbose_name='ادرس لینک')
    category = models.ManyToManyField(Category,related_name='category',verbose_name='دسته بندی')
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
    
    def jupdated(self):
        return jalali_converter(self.updated)

    jpublish.short_description = 'تاریخ انتشار'

    jupdated.short_description = 'تاریخ بروز رسانی'

    