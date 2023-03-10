from django import forms
from .models import Employee, Depatment
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class LoginForm(forms.ModelForm):
    '''login form '''
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        '''login form meta class'''
        model = User
        fields = ['email','password']

class EmployeeForm(forms.ModelForm):
    ''' employee form '''
    # password = forms.CharField(widget=forms.PasswordInput)
    # DEPATMENTS_CHOICES = [(i.id,i.name) for i in Depatment.objects.all()]
    # name = forms.CharField(choices=DEPATMENTS_CHOICES,default="HR",max_length=20)
    select_role = forms.ModelMultipleChoiceField( widget=forms.CheckboxSelectMultiple,queryset=Depatment.objects.all(), required=True)

    # select_role = Depatment.objects.filter()
    # print(select_role)
    class Meta:
        '''emplyoee meta class'''
        model = Employee
        fields = ['email','first_name','last_name','select_role']

    def clean(self):
        '''clean method for email'''
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        select_role = cleaned_data.get('select_role')
        if not first_name:
            raise forms.ValidationError({"first_name":"enter first name"})

        if not select_role:
            raise forms.ValidationError({"select_role":"select any role"})

    def save(self, commit=False):
        '''save password method'''
        instance = super().save(commit=True)
        # print("instance****", instance.email)
        instance.set_password(instance.email +'@1234')
        # print(instance.password)
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-sm'
        # self.fields['select_role'].widget.attrs['class'] = 'form-check-label'

class EmployeeEdit(forms.ModelForm):
    '''employee edit form'''
    select_role = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Depatment.objects.all())

    class Meta:
        '''edit employee meta class'''
        model = Employee
        fields = ['email','first_name','last_name','select_role']

class SendEmail(forms.ModelForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        fields = ['email']