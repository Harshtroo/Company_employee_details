from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import EmployeeForm,EmployeeEdit
from .models import Employee
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView,View
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
    '''logout class'''
    # success_url_allowed_hosts = 'home'
    # def post(self, request, *args, **kwargs):
    #     messages.error(request=self.request, message="successfully create")
    #     return super().post(request, *args, **kwargs)
    pass


@method_decorator(login_required(login_url="/login/"), name='dispatch')
class EmployeeList(ListView):
    ''' show employee list'''
    template_name = 'employee_list.html'
    model = Employee
    queryset = Employee.objects.filter(is_deleted = False)
    context_object_name = 'employee'

    # def get(self,*args,**kwargs):
    #     # breakpoint()
    #     queryset = Employee.objects.filter(is_deleted = False)
    #     return queryset
    # select_role_count = Employee.objects.get(select_role = re)

class CreateEmployee(CreateView):
    '''employee create'''
    model = Employee
    form_class = EmployeeForm
    template_name = 'add_employee.html'

    def post(self, request, *args, **kwargs):
        '''create employee post request'''
        # messages.error(request=self.request, message="Email already Exists.")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        ''' create employee form valid or not.'''
        form.save()
        messages.success(request=self.request, message="successfully create")
        # messages.error(request=self.request, message="email already exists")
        super().form_valid(form)
        return redirect('employee_list')

    def get_success_url(self):
        ''''creae employee form and redirect url'''
        return reverse_lazy('employee_list')


class EmployeeEditForm(UpdateView):
    '''employee edit form class'''
    template_name ='employee_edit.html'
    form_class = EmployeeEdit
    model = Employee
    success_url = reverse_lazy('employee_list')

    def post(self,request,*args,**kwagrs):
        '''employee edit post method'''
        messages.success(request=self.request, message="successfully Updated")
        return super().post(request,*args,**kwagrs)
    # def get(self,request,*args,**kwagrs):
    #     '''employee form get request. '''
    #     context = {}
    #     context['form'] = EmployeeEdit(instance=Employee.objects.get(id=kwagrs['pk']))
    #     return render(request,"employee_edit.html",context)

    # def post(self,request, *args, **kwargs):
    #     '''employee form post request.'''
    #     # context = {}
    #     # breakpoint()
    #     form = self.get_form()
    #     print(form)
    #     form = EmployeeEdit(request.POST,instance=Employee.objects.get(id=kwargs['pk']))
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request=self.request, message="successfully updated")
    #     return redirect('employee_list')

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