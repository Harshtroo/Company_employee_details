from django import forms
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class EmployeeForm(forms.ModelForm):
    ''' employee form '''
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        '''emplyoee meta class'''
        model = Employee
        fields = ['username','depatments', "password"]
    
    def save(self,*args, **kwargs):
        self.instance.password = make_password(self.cleaned_data['password1'])
        super().save(*args,**kwargs)
        try :
            user = User.object.get(username="username")
            user.set_password('email')
            user.save()
        
    def set_defult_password(self):
        pass