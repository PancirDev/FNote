from django.db import models


class Customer(models.Model):
    company = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=17)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200)
    note = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['company']

    def __str__(self):
        return self.company


class Project(models.Model):
    name = models.CharField(max_length=150)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    description = models.CharField(max_length=300)
    deadline = models.DateField()
    price = models.FloatField()
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    state_text = models.CharField(max_length=20)
    estimate = models.FloatField()
    deadline = models.DateField()

    def __str__(self):
        return self.name
