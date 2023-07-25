from django.shortcuts import render
from .models import AboutUs
# Create your views here.


def aboutus(request):
    
    aboutus = AboutUs.objects.first()
    context ={
        'aboutus': aboutus
    }
    return render(request,'aboutus.html',context)