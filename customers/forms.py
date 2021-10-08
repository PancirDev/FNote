from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['company', 'full_name', 'phone', 'email', 'address', 'note']
        labels = {
            'company': 'Организация',
            'full_name': 'Контактное лицо',
            'phone': 'Телефон',
            'email': 'Email',
            'address': 'Адрес',
            'note': 'Дополнительно',
        }
        widgets = {
            'company': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Организация'
            }),
            'full_name': TextInput(attrs={
                'class': 'form-control',
                'label': 'Контактное лицо',
                'placeholder': 'Контактное лицо'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'note': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительно',
                'rows': '2',
            }),
        }


class UserInfoForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['company', 'full_name', 'phone', 'email', 'address', 'note']
        labels = {
            'company': 'Организация',
            'full_name': 'Контактное лицо',
            'phone': 'Телефон',
            'email': 'Email',
            'address': 'Адрес',
            'note': 'Дополнительно',
        }
        widgets = {
            'company': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Организация'
            }),
            'full_name': TextInput(attrs={
                'class': 'form-control',
                'label': 'Контактное лицо',
                'placeholder': 'Контактное лицо'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'note': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительно',
                'rows': '2',
            }),
        }
        # 'style': 'max-width: 300px;',



    # company = models.CharField(max_length=150, unique=True)
    # full_name = models.CharField(max_length=150)
    # phone = models.CharField(max_length=17)
    # email = models.EmailField()
    # address = models.CharField(max_length=200)
    # note = models.CharField(max_length=300)

