from django.urls import path

from . import views
from .views import CustomerDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('detail/<int:pk>/', views.det, name='det'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
]
