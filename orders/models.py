from django.db import models
from tabel.models import Table
from menu.models import Menu
from django.utils import timezone
from jdatetime import datetime as jdatetime
# Create your models here.

class Order(models.Model):

    PAYMENT=(
        ('naghd','پرداخت نقدی'),
        ('online','پرداخت آنلاین'),
    )
    customer_name = models.CharField(max_length=250, verbose_name='نام مشتری')
    customer_number = models.CharField(max_length=25, verbose_name='شماره سفارش')
    order_total = models.IntegerField(verbose_name= 'مبلغ کل', default=0)
    is_paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    payment_method = models.CharField(max_length=20, choices=PAYMENT, default='online', verbose_name='نحوه پرداخت')
    payment_time = models.DateTimeField(auto_now_add=True, verbose_name='زمان پرداخت')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='میز')
    

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"

    def jdatetime_payment_time(self):
        return jdatetime.fromgregorian(datetime=timezone.localtime(self.payment_time)).strftime('%Y/%m/%d - ساعت: %H:%M:%S')
    jdatetime_payment_time.short_description = '  زمان پرداخت شمسی'

    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='آیتم منو')
    quantity = models.IntegerField(verbose_name='تعداد')
    item_price = models.IntegerField(verbose_name='قیمت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='زمان')

    class Meta:
        verbose_name = "آیتم سفارش"
        verbose_name_plural = "آیتم های سفارش"

    def __str__(self):
        return f'{self.menu.titel} - {self.quantity}'

    def save(self, *args, **kwargs):
        # محاسبه قیمت آیتم براساس تعداد
        self.item_price = self.quantity * self.menu.price
        super().save(*args, **kwargs)

        # بروزرسانی قیمت کل سفارش با اضافه کردن قیمت آیتم جدید به قیمت های آیتم های دیگر
        order_items = OrderItem.objects.filter(order=self.order)
        total_price = sum([item.item_price for item in order_items])
        self.order.order_total = total_price
        self.order.save()