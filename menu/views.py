from django.shortcuts import render ,get_object_or_404 , redirect
from .models import Menu
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from comment.forms import CommentModelForm
from comment.models import Comment



# Create your views here.
def menu(request,category_slug=None):

    categories = None
    paged_items = None
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        items = Menu.objects.filter(category=categories).order_by('id')
        paginator = Paginator(items, 3)
        page = request.GET.get('page')
        paged_items = paginator.get_page(page)
        items_count = items.count()
    else:
        items = Menu.objects.all().order_by('id')
        paginator = Paginator(items, 3)
        page = request.GET.get('page')
        paged_items = paginator.get_page(page)
        items_count = items.count()

    context = {
        'items': paged_items,
        'items_count':items_count,
    }
    return render(request, "home.html", context=context)

def item_detail(request,category_slug,item_slug):
               
    try:
        single_item = Menu.objects.get(category__slug=category_slug, slug=item_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), menu=single_item).exists()

    except Exception as e:
        raise e
    
    form_class = CommentModelForm
    comments = Comment.objects.filter(is_active=True,menu=single_item)
    comment_count = comments.count()
    if request.method == "POST":
        form = form_class(data=request.POST)
        if form.is_valid():
            comment_obj = form.save(commit=False)
            comment_obj.menu = single_item

            comment_obj.save()
            request.session['current_url']=request.get_full_path()
            return redirect('messages')
            
    context ={
        'single_item':single_item,
        'in_cart':in_cart,
        'comments':comments,
        'comment_count': comment_count
        
    }

    return render(request,'item_detail.html',context=context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            items = Menu.objects.order_by('id').filter(titel__icontains=keyword)
            items_count = items.count()
    context ={
        'items':items,
        'items_count': items_count,
        
    }
    return render (request, 'home.html',context)

def messages(request):
    url = request.session.get('current_url')
    if not url:
        raise Http404
    request.session['current_url'] = None
    context ={
        'url':url,
    }
    return render(request,'messages.html',context)
