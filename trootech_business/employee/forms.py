from django import forms
from .models import Employee
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    ''' employee form '''
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        '''emplyoee meta class'''
        model = Employee
        fields = ['email','first_name','last_name','depatments','password']

    # def create_user(self,email,password):
    #     if not email :
    #         raise ValueError('The Email must be set')
    #     else:
    #         email = self.normalize_email(email)
    #         user = self.model(email=email)
    #         user.set_password(email)
    #         user.save()
    #         return user

class LoginForm(forms.ModelForm):
    '''login form '''
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        '''login form meta class'''
        model = User
        fields = ['email','password']