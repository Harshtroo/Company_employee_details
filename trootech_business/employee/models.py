from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

class Company(models.Model):
    ''' company name model'''
    name =models.CharField(max_length=100)

class Depatment(models.Model):
    '''employee details model'''
    DEPATMENTS_CHOICES = {
        ('DEVELOPER','Developer'),
        ('HR','HR'),
        ('ADMIN','Admin'),
        ('CTO','CTO')
    }
    depatments = models.CharField(choices=DEPATMENTS_CHOICES,max_length=100)             

    def __str__(self):
        return self.depatments

class Employee(AbstractUser):
    '''this class employee model'''
    username = models.CharField(max_length=150, blank=True, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    depatments = models.ManyToManyField(Depatment)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def save(self,*args, **kwargs):
        '''save password method'''
        self.password = make_password(self.email +'@1234')
        super().save(*args,**kwargs)

    def soft_delete(self):
        '''soft delete funcction'''
        self.is_deleted = True
        self.save()
    