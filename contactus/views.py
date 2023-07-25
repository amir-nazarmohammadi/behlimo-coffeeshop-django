from django.shortcuts import render
from .models import ContactUs
# Create your views here.

def contactus(request):
    
    contactus = ContactUs.objects.first()
    context ={
        'contactus': contactus
    }
    return render(request,'contactus.html',context)