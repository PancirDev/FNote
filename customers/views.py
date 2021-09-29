from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Customer

#__all__ = (
#    'home',
#)


def home(request):
    qs = Customer.objects.all()
    context = {'objects_list': qs}
    return render(request, 'customers/home.html', context)


def index(request):
    return HttpResponse("Hello, world. I'm index | path('' ")


def det(request, pk=None):
    return HttpResponse("Hello, world. I'm det | path('detail/<int:pk>/' ")


class CustomerDetailView(DetailView):
    model = Customer
    # queryset = Customer.objects.all()
    # template_name = 'customers/detail.html'


class CustomerListView(ListView):
    model = Customer
