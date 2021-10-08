from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from .forms import CustomerForm, UserInfoForm
from .models import Customer, Project, Task


class CustomerDetailView(DetailView):
    model = Customer
    # template_name = 'customers/customer_detail.html'
    # context_object_name = 'customer'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.filter(customer=context['customer'])
        return context


class CustomerListView(ListView):
    model = Customer
    # template_name = 'customers/customer_list.html'
    context_object_name = 'customers_list'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects_list'


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.filter(project=context['project'])
        return context


class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerForm
    # form_class = UserInfoForm
    template_name = 'customers/customer_update.html'
    success_url = reverse_lazy('customers:list')
    success_message = 'Клиент успешно отредактирован'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.filter(customer=context['customer'])
        return context
