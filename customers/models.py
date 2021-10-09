from django.db import models


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
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    description = models.CharField(max_length=300)
    # state = models.CharField(max_length=30)
    # state = models.ForeignKey(Task, on_delete=models.CASCADE)
    deadline = models.DateField()
    price = models.FloatField()
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    # project | state_index | state_text | estimate | deadline_date
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    description = models.CharField(max_length=300)
    state_text = models.CharField(max_length=20)
    estimate = models.FloatField()
    deadline = models.DateField()
    # ready = models.BooleanField(default=False)

    def __str__(self):
        return self.description
