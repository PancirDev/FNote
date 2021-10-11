from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from .forms import CustomerForm, ProjectForm, TaskForm
from .models import Customer, Project, Task


class CustomerCreate(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_update.html'
    success_message = 'Контрагент успешно создан'

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
    success_message = 'Контрагент успешно отредактирован'

    def get_success_url(self):
        customer_id = self.kwargs['pk']
        return reverse_lazy('customers:update', kwargs={'pk': customer_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['customer'].project_set.all()
        return context


class CustomerDelete(SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = 'customers/customer_delete.html'
    success_url = reverse_lazy('customers:list')
    success_message = 'Контрагент успешно удален'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context['object_list'] = context['project'].task_set.all()
        return context


class ProjectDelete(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'customers/project_delete.html'
    success_url = reverse_lazy('customers:projects_list')
    success_message = 'Проект успешно удален'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['project'].task_set.all()
        return context


class ProjectList(ListView):
    model = Project
    context_object_name = 'objects_list'
    template_name = 'customers/projects_list.html'


class TaskUpdate(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'customers/task_update.html'
    success_message = 'Задача успешно отредактирована'

    def get_success_url(self):
        task_id = self.kwargs['pk']
        return reverse_lazy('customers:task_update', kwargs={'pk': task_id})


class TaskCreate(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'customers/task_update.html'
    success_message = 'Задача успешно создана'

    def get_success_url(self):
        task_id = self.object.pk
        return reverse('customers:task_update', kwargs={'pk': task_id})

    def get_form_kwargs(self, *args, **kwargs):
            kwargs = super(TaskCreate, self).get_form_kwargs(*args, **kwargs)
            return kwargs


class TaskDelete(SuccessMessageMixin, DeleteView):
    model = Task

    def get_success_url(self):
        project_id = self.object.project.pk
        return reverse('customers:project_update', kwargs={'pk': project_id})

    def get_form_kwargs(self, *args, **kwargs):
            kwargs = super(TaskDelete, self).get_form_kwargs(*args, **kwargs)
            return kwargs

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Задача успешно удалена')
        return self.post(request, *args, **kwargs)
