from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_customer, name='register_customer'),
]

