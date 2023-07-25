from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from menu.models import Menu
from .models import Cart, CartItem
from tabel.models import Table

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
       cart = request.session.create()
    return cart

def add_cart(request, menu_id):
    menu = Menu.objects.get(id=menu_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    
    cart.save()

    try:
        cart_item = CartItem.objects.get(menu=menu, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            menu = menu,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')

def remove_cart(request,menu_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    menu = get_object_or_404(Menu, id=menu_id)
    cart_item = CartItem.objects.get(menu=menu, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,menu_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    menu = get_object_or_404(Menu, id=menu_id)
    cart_item = CartItem.objects.get(menu=menu, cart=cart)
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.menu.price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    
        
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,

    }
    return render(request, 'cart.html', context=context)

def checkout(request,total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        tabels = Table.objects.exclude(is_reserved=True)    
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.menu.price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    
        
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tabels': tabels,
    }
    return render (request, 'checkout.html',context)