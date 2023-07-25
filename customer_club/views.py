from django.shortcuts import render
from .forms import CustomerForm
from django.contrib import messages


def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = CustomerForm()
    return render(request, 'home.html', {'form': form})
