from django.contrib import admin
from .models import Order, OrderItem
import locale
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['item_price']

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['customer_name', 'order_total_formatted', 'is_paid', 'payment_method', 'payment_time', 'table', 'jdatetime_payment_time']
    list_filter = ['is_paid', 'payment_method', 'payment_time']
    search_fields = ['customer_name']
    readonly_fields = ['order_total']

    def order_total_formatted(self, obj):
        locale.setlocale(locale.LC_ALL, 'fa_IR')
        return format(obj.order_total, ',d') + ' تومان'
    order_total_formatted.short_description = 'مبلغ سفارش'    
    
admin.site.register(Order, OrderAdmin)