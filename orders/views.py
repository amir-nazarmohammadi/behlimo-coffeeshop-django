from django.shortcuts import render, redirect
import datetime
from cart.models import CartItem
from .models import Order, OrderItem
from .forms import OrderForm


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def place_order(request, total=0, quantity=0):
    cart_items = CartItem.objects.filter(cart__cart_id=_cart_id(request), is_active=True)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('menu')

    for cart_item in cart_items:
        total += (cart_item.menu.price * cart_item.quantity)
        quantity += cart_item.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)      
        if form.is_valid():

            data = Order()          
            data.customer_name = form.cleaned_data['customer_name']
            data.is_paid = True
            table = form.cleaned_data.get('table')
            data.table = table
            table.is_reserved = True
            table.save()
            data.order_total = total         
            data.save()
            
                        # ذخیره آیتم های سفارش جدید
            for cart_item in cart_items:
                order_item = OrderItem()
                order_item.order = data  # پر کردن کلید خارجی
                order_item.menu = cart_item.menu
                order_item.quantity = cart_item.quantity
                order_item.save()
            


            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_data = d.strftime("%Y%m%d")
            customer_number = current_data + str(data.id)
            data.customer_number = customer_number
            data.save()
            
            CartItem.objects.filter(cart__cart_id=_cart_id(request), is_active=True).delete()
            return redirect('checkout')

        else:
            error_message = 'فرم نامعتبر است. لطفاً اطلاعات را به درستی وارد کنید.'
            return render(request, 'checkout.html', {'error_message': error_message , 'form':form})
    else:
        error_message = 'این صفحه فقط برای درخواست‌های POST قابل دسترسی است.'
        return render(request, 'checkout.html', {'error_message': error_message,'form':form})


