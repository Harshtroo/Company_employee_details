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
        ('HR','HR'),
        ('DEVLOPER','Developer'),
        ('ADMIN','Admin'),
        ('CTO','CTO')
    }
    name = models.CharField(choices=DEPATMENTS_CHOICES,default="HR",max_length=20)

    def __str__(self):
        return self.name

class Employee(AbstractUser):
    '''this class employee model'''
    username = models.CharField(max_length=150, blank=True, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    select_role = models.ManyToManyField(Depatment)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        '''soft delete funcction'''
        self.is_deleted= True
        self.save()
    
    @property 
    def get_roles(self):
        return [select_value['name'] for select_value in self.select_role.values('name')]
