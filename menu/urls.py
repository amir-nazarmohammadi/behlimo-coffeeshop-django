from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('search/',views.search, name='search'),
    path('<slug:category_slug>/', views.menu, name='menu_by_category'),
    path('<slug:category_slug>/<slug:item_slug>/', views.item_detail, name='item_detail'),
    path('messages', views.messages, name='messages'),
    


]

