from django.db import models

# Create your models here.

class Table(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام میز')
    is_reserved = models.BooleanField(default=False, verbose_name='رزرو شده است')

    class Meta:
        verbose_name = "میز"
        verbose_name_plural = "میزها"

    def __str__(self):
        return self.name