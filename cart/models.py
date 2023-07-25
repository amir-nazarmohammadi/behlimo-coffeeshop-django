from django.db import models
from menu.models import Menu

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, verbose_name='شناسه سبد',null=True)
    dete_added = models.DateField(auto_now_add=True,verbose_name='تاریخ ادد')

    class Meta:
        verbose_name = "سبد"
        verbose_name_plural = "سبد ها"

    def __str__(self):
        return self.cart_id

    
class CartItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='آیتم منو')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='سبد')
    quantity = models.IntegerField(verbose_name='تعداد')
    is_active = models.BooleanField(default=True,  verbose_name='فعال')

    class Meta:
        verbose_name = "آیتم سبد"
        verbose_name_plural = "آیتم های سبد"

    def sub_total(self):
        return self.menu.price * self.quantity

    def __str__(self):
        return self.menu.titel
