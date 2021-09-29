from django.contrib import admin
from django.urls import include, path

# from customers.views import home

urlpatterns = [
    path('customers/', include('customers.urls', 'customers')),
    # path('home/', home),
    path('admin/', admin.site.urls),
]