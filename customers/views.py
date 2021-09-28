from django.http import HttpResponse
#from django.shortcuts import render

#from customers.models import Customer

#__all__ = (
#    'home',
#)


#def home(request):
#    qs = Customer.objects.all()
#    context = {'objects_list': qs}
#    return render(request, 'customers/home.html', context)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
