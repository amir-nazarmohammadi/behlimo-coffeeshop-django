from django.db import models

# Create your models here.
class ContactUs(models.Model):
    mobile = models.CharField(max_length=15,null=True,blank=True,verbose_name="شماره موبایل")
    phone = models.CharField(max_length=15,null=True,blank=True,verbose_name="شماره تلفن")
    email = models.CharField(max_length=50,null=True,blank=True,verbose_name="ایمیل")
    address = models.CharField(max_length=200,null=True,blank=True,verbose_name="آدرس")
    instagram = models.CharField(max_length=40,null=True,blank=True,verbose_name="اینستاگرام")
    whatsapp = models.CharField(max_length=40,null=True,blank=True,verbose_name="واتساپ")
    map_addres = models.CharField(max_length=350,null=True,blank=True,verbose_name="آدرس نقشه")
    
    

    class Meta:
        verbose_name = ("تنظیمات تماس  با ما")
        verbose_name_plural = ("تنظیمات تماس با ما")

    def __str__(self):
        return "تنظیمات تماس"

