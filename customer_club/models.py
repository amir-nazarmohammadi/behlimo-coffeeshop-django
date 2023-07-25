from django.db import models

# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=50, verbose_name=' نام و نام خانوادگی')
    phone_number = models.CharField(max_length=20, verbose_name='شماره تلفن')

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "باشگاه مشتریان"

    def __str__(self):
        return self.full_name
