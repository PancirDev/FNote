from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('customers/', include('customers.urls', 'customers')),
    path('admin/', admin.site.urls),
]
