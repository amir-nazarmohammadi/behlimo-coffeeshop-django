from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'phone_number')
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'phone_number': 'شماره تلفن',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موبایل'}),
        }
