from django.urls import path

from customers.views import *

urlpatterns = [
    path('', home, name='home'),
]
