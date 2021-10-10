from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Customer, Project


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
                'placeholder': 'Организация',
            }),
            'full_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Контактное лицо',
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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'customer', 'description', 'deadline', 'price', 'paid', 'completed']
        labels = {
            'name': 'Проект',
            'customer': 'Контрагент',
            'description': 'Описание',
            'deadline': 'Срок сдачи',
            'price': 'Стоимость',
            'paid': 'Оплачен',
            'completed': 'Завершен',
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Проект',
            }),
            'customer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Контрагент',
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }
