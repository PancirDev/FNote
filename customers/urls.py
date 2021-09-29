from django.urls import path

from . import views
from .views import CustomerDetailView, CustomerListView

app_name = 'customers'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.CustomerListView.as_view(), name='list'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),

    path('home/', views.home, name='home'),
    path('detail/<int:pk>/', views.det, name='det'),

]
