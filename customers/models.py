import datetime

from django.db import models
from django.utils import timezone


class Customer(models.Model):
    company = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    note = models.CharField(max_length=300)

    def __str__(self):
        return self.company


class Project(models.Model):
    name = models.CharField(max_length=150)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    state = models.CharField(max_length=30)
    deadline = models.DateField()
    price = models.FloatField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.deadline >= timezone.now() - datetime.timedelta(days=1)
