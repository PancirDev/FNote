from django.views.generic import DetailView, ListView
from .models import Customer


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'

