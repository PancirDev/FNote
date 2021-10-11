from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from .forms import CustomerForm, ProjectForm
from .models import Customer, Project, Task


class CustomerCreate(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_update.html'
    success_message = 'Клиент успешно создан'

    def get_success_url(self):
        customer_id = self.object.pk
        return reverse('customers:update', kwargs={'pk': customer_id})

    def get_form_kwargs(self, *args, **kwargs):
            kwargs = super(CustomerCreate, self).get_form_kwargs(*args, **kwargs)
            return kwargs


class CustomerUpdate(SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_update.html'
    success_message = 'Клиент успешно отредактирован'

    def get_success_url(self):
        customer_id = self.kwargs['pk']
        return reverse_lazy('customers:update', kwargs={'pk': customer_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['project_list'] = Project.objects.filter(customer=context['customer'])
        context['object_list'] = context['customer'].project_set.all()
        return context


class CustomerDelete(SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = 'customers/customer_delete.html'
    success_url = reverse_lazy('customers:list')
    success_message = 'Клиент успешно удален'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['project_list'] = Project.objects.filter(customer=context['customer'])
        context['object_list'] = context['customer'].project_set.all()
        return context


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers_list'


class ProjectCreate(SuccessMessageMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'customers/project_update.html'
    success_message = 'Проект успешно создан'

    def get_success_url(self):
        project_id = self.object.pk
        return reverse('customers:project_update', kwargs={'pk': project_id})

    def get_form_kwargs(self, *args, **kwargs):
            kwargs = super(ProjectCreate, self).get_form_kwargs(*args, **kwargs)
            return kwargs


class ProjectUpdate(SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'customers/project_update.html'
    success_message = 'Проект успешно отредактирован'

    def get_success_url(self):
        project_id = self.kwargs['pk']
        return reverse_lazy('customers:project_update', kwargs={'pk': project_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['project_list'] = Project.objects.filter(customer=context['customer'])
        # context['project_list'] = context['customer'].project_set.all()
        # context['object_list'] = Task.objects.filter(project=context['project'])
        context['object_list'] = context['project'].task_set.all()
        return context


class ProjectDelete(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'customers/project_delete.html'
    success_url = reverse_lazy('customers:projects_list')
    success_message = 'Проект успешно удален'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['project_list'] = Project.objects.filter(customer=context['customer'])
        # context['project_list'] = context['customer'].project_set.all()
        # context['object_list'] = Task.objects.filter(project=context['project'])
        context['object_list'] = context['project'].task_set.all()
        return context


class ProjectList(ListView):
    model = Project
    context_object_name = 'objects_list'
    template_name = 'customers/projects_list.html'
