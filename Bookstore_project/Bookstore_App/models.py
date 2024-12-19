import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

class CustomUser(AbstractUser):
    # Add custom fields if needed
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Super User"
        verbose_name_plural = "Super Users"

# Create your models here.
class Staff(CustomUser):
    # Add custom fields if needed
    position = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"

    def __str__(self):
        return self.first_name + " " + self.last_name  # You can return any meaningful representation

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    customer = models.ForeignKey('Customer', related_name='addresses', on_delete=models.CASCADE)  # Many addresses can belong to one customer
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country} - {self.postal_code}"

class Customer(CustomUser):
    cash = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.first_name + " " + self.last_name
