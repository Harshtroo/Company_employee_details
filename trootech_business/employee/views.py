from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import EmployeeForm,EmployeeEdit
from .models import Employee
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView,View
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse,reverse_lazy
from .mixin import RoleRequiredMixin,EditProfilemixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(TemplateView):
    '''home class'''
    template_name = 'home.html'

class Login(LoginView):
    '''login class '''
    template_name = 'login.html'
    success_message = "Thing was deleted successfully."

class Logout(LogoutView):
    '''logout class'''
    pass

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class EmployeeList(ListView):
    ''' show employee list'''
    template_name = 'employee_list.html'
    model = Employee
    queryset = Employee.objects.filter(is_deleted = False)
    context_object_name = 'employee'

class CreateEmployee(RoleRequiredMixin, CreateView):
    '''employee create'''
    model = Employee
    form_class = EmployeeForm
    template_name = 'add_employee.html'

    def post(self, request, *args, **kwargs):
        '''create employee post request'''
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        ''' create employee form valid or not.'''
        form.save()
        messages.success(request=self.request, message="successfully create")
        super().form_valid(form)
        return redirect('employee_list')

    def get_success_url(self):
        ''''creae employee form and redirect url'''
        return reverse_lazy('employee_list')

class EmployeeEditForm(LoginRequiredMixin,UpdateView):
    '''employee edit form class'''
    template_name ='employee_edit.html'
    form_class = EmployeeEdit
    model = Employee
    success_url = reverse_lazy('employee_list')

    def post(self,request,*args,**kwagrs):
        '''employee edit post method'''
        if 'DEVELOPER' in request.user.get_roles:
            if request.user.id == kwagrs.get('pk'):
                # print(request.user.id)
                messages.success(request=self.request, message="Successfully updated")
                return super().post(request,*args,**kwagrs)
        elif request.user.has_access:
            messages.success(request=self.request, message="Successfully updated")
            return super().post(request,*args,**kwagrs)
        messages.error(request=self.request, message="You are not Authorised")
        return redirect(reverse("employee_list"))

class EmployeeDelete(View):
    '''employee delete class'''
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')

    def post(self, request, *args, **kwargs):
        ''''employee delete post method'''
        employee = Employee.objects.get(id=kwargs['pk'])
        employee.is_deleted = True
        employee.save()
        messages.success(request=self.request, message="successfully Deleted.")
        return HttpResponseRedirect(self.success_url)