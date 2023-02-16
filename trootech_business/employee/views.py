from django.shortcuts import render,redirect
from .forms import LoginForm,EmployeeForm,EmployeeEdit
from .models import Employee
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import TemplateView, FormView,RedirectView,ListView,DetailView,UpdateView,CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse,reverse_lazy

# Create your views here.

class Home(TemplateView):
    '''home class'''
    template_name = 'home.html'

class Login(LoginView):
    '''login class '''
    # form_class = LoginForm
    # authentication_form = LoginForm
    template_name = 'login.html'
    # success_url = '/employee_list/'
    # redirect_authenticated_user = True
    success_message = "Thing was deleted successfully."


class Logout(LogoutView):
    pass


@method_decorator(login_required(login_url="/login/"), name='dispatch')
class EmployeeList(ListView):
    template_name = 'employee_list.html'
    model = Employee
    queryset =Employee.objects.all()
    context_object_name = 'employee'

# class EmployeeEdit(RedirectView):
#     permanent = False
#     query_string = True
#     pattern_name = 'login'

#     def get_redirect_url(self, *args, **kwargs):
#         Login(self.request)
#         return super(Login,self).get_redirect_url(*args, **kwargs)

class CreateEmployee(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'add_employee.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            print("cleaned_data: ", form.cleaned_data)
            # remove roles from dict
            # find the each role's id from department table 
            # save the form 
            # many to many field update 
            # save the form again
            
            # form.save()
            return redirect(reverse("employee_list"))
        print("form", form)
        return redirect(reverse("employee_list"))
            
    def get_success_url(self):
        return reverse_lazy('employee_list')


class EmployeeEditForm(DetailView,UpdateView):
    template_name ='employee_edit.html'
    form_class = EmployeeEdit
    model = Employee

    def get(self,request,e_id,*args,**kwagrs):
        context = {}
        context['user_form'] = EmployeeEdit(instance=Employee.objects.get(id=e_id))
        return render(request,"edit.html",context)
    def post(self,request,e_id, *args, **kwargs):
        # context = {}
        form = self.get_form()
        form = EmployeeEdit(request.POST,instance=Employee.objects.get(id=e_id))
        if form.is_valid():
            form.save()
        return redirect('employee_list')