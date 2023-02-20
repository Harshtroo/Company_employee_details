from django.shortcuts import render,redirect
from .forms import LoginForm,EmployeeForm,EmployeeEdit
from .models import Employee
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
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
    # success_url_allowed_hosts = 'home'
    # def post(self, request, *args, **kwargs):
    #     messages.error(request=self.request, message="successfully create")
    #     return super().post(request, *args, **kwargs)
    pass


@method_decorator(login_required(login_url="/login/"), name='dispatch')
class EmployeeList(ListView):
    template_name = 'employee_list.html'
    model = Employee
    queryset =Employee.objects.all()
    context_object_name = 'employee'

    
    # select_role_count = Employee.objects.get(select_role = re)
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
        # select_role_id = request.POST.getlist('select_role')
        # print(select_role_id)
        # form = Employee(request.POST)
        # employee = request.POST.getlist('employee')
        # print(employee)
        # if form.is_validd():
        #     role = form.save()
        #     role.user = request.user
        #     role.save()
        # else:
        #     form = Employee()
        # a = Employee.objects.all()
        # for i in a:
        #     print(i.id)
        # print(a)
        # messages.error(request=self.request,message="SBcsiiocd")
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        form.save()
        messages.success(request=self.request, message="successfully create")
        # messages.error(request=self.request, message="email already exists")
        super().form_valid(form)
        return redirect('employee_list')

    def get_success_url(self):
        return reverse_lazy('employee_list')


class EmployeeEditForm(DetailView,UpdateView):
    template_name ='employee_edit.html'
    form_class = EmployeeEdit
    model = Employee
    success_url = 'employee_list'

    def get(self,request,e_id,*args,**kwagrs):
        context = {}    
        context['form'] = EmployeeEdit(instance=Employee.objects.get(id=e_id))
        return render(request,"employee_edit.html",context)

    def post(self,request,e_id, *args, **kwargs):
        # context = {}
        form = self.get_form()
        form = EmployeeEdit(request.POST,instance=Employee.objects.get(id=e_id))
        if form.is_valid():
            form.save()
            messages.success(request=self.request, message="successfully updated")
        return redirect('employee_list')

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')