from django.shortcuts import render,redirect
from .forms import LoginForm,EmployeeForm
from .models import Employee
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import TemplateView, FormView,RedirectView,ListView,DetailView,UpdateView
from django.contrib.auth.decorators import login_required
# Create your views here.

class Home(TemplateView):
    '''home class'''
    template_name = 'home.html'

class Login(LoginView):
    '''login class '''
    # form_class = LoginForm
    template_name = 'login.html'
    sucess_url = 'employee_list/'
    # redirect_authenticated_user = True

    # def get_success_url(self,*args,**kwagrs):
    #     return self.success_url('employee_list')

    def form_invalid(self,form):
        '''this method use invalid form '''       
        messages.error(self.request,"Invalid username or password.")
        return self.render_to_response  (self.get_context_data(form=form))

# class Logout(RedirectView):
#     '''logout class'''
#     permanent = False
#     query_string = True
#     pattern_name = 'home'

#     def get_rediect_url(self,*args,**kwargs):
#         '''logout function'''
#         if self.request.user.is_authenticated():
#             logout(self.request)
#         return super(Logout,self).get_redirect_url(*args,**kwargs)

class EmployeeDetails(ListView):
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

class CreateEmployee(FormView):
    form_class = EmployeeForm
    template_name = 'add_employee.html'


class EmployeeEdit(DetailView,UpdateView):
    pass