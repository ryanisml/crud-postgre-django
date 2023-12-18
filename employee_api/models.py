from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    position = models.CharField(max_length=100)
    id_employee = models.CharField(max_length=6, unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)