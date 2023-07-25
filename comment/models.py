from django.db import models
from menu.models import Menu
from django.utils import timezone
from jdatetime import datetime as jdatetime
# Create your models here.

class Comment(models.Model):
    menu = models.ForeignKey(to =Menu, on_delete=models.CASCADE, verbose_name="آیتم منو", related_name="comment")
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    message = models.TextField(verbose_name="متن")
    time = models.DateTimeField(auto_now_add=True, verbose_name='زمان نظر')
    is_active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال" )
    

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return self.full_name
    
    def comment_time(self):
        return jdatetime.fromgregorian(datetime=timezone.localtime(self.time)).strftime('%Y/%m/%d - ساعت: %H:%M:%S')
    comment_time.short_description = 'زمان'


