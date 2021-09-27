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
