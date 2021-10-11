from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea, NumberInput, DateInput, CheckboxInput

from .models import Customer, Project, Task


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
            'price': 'Сумма',
            'paid': 'Оплачен',
            'completed': 'Завершен',
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Проект',
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Контрагент',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
                'rows': '2',
            }),
            'deadline': DateInput(attrs={
                'class': 'form-control',
                'placeholder': '2021-12-31',
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'к оплате',
            }),
            'paid': CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'completed': CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'project', 'state_text', 'estimate', 'deadline']
        labels = {
            'name': 'Задача',
            'project': 'Проект',
            'state_text': 'Статус',
            'estimate': 'Часы',
            'deadline': 'Срок сдачи',
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задача',
            }),
            'project': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Проект',
            }),
            'state_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
            }),
            'estimate': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Часы',
            }),
            'deadline': DateInput(attrs={
                'class': 'form-control',
                'placeholder': '2021-12-31',
            }),
        }
