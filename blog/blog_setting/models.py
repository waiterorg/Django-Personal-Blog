from django.db import models

# Create your models here.

class settings(models.Model):
    site_name = models.CharField(max_length=100,verbose_name='نام سایت')
    site_logo = models.ImageField(upload_to = 'site_image',verbose_name='لوگو سایت')
    site_copyright = models.CharField(max_length=120,verbose_name='قانون کپی رایت / صاحب سایت')
    short_description = models.CharField(max_length=150,verbose_name='معرفی سایت')

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'
    
    def __str__(self):
        return self.site_name
