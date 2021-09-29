from django.views.generic import DetailView, ListView
from .models import Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerListView(ListView):
    model = Customer
