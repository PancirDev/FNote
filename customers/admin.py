from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['company', 'full_name', 'phone']
    search_fields = ['company', 'full_name']


admin.site.register(Customer, CustomerAdmin)
