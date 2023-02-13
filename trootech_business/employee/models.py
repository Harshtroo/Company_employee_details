from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.
from django.contrib.auth.models import AbstractBaseUser




class Company(models.Model):
    ''' company name model'''
    name =models.CharField(max_length=100)

class Depatment(models.Model):
    '''employee details model'''
    DEPATMENTS_CHOICES = {
        ('Developer','Developer'),
        ('HR','HR'),
        ('Admin','Admin'),
        ('CTO','CTO')
    }
    depatments = models.CharField(choices=DEPATMENTS_CHOICES,max_length=100)             #CharField(choices=DEPATMENTS_CHOICES,max_length=6)

    def __str__(self) -> str:
        return self.depatments

class Employee(AbstractUser):
    DEPATMENTS_CHOICES = {
        ('DEVELOPER','Developer'),
        ('HR','HR'),
        ('ADMIN','Admin'),
        ('CTO','CTO')
    }

    username = models.CharField(max_length=150, blank=True, unique=False)
    email = models.EmailField(max_length=255, unique=True)
    depatments = models.ManyToManyField(Depatment)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

    # depatments = models.CharField(choices=DEPATMENTS_CHOICES,max_length=10)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ["username"]


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = 'email'
