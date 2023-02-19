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

    # def post(slef,request):
    #     print("dcjdbvdvdbv")
    #     employee_obj = Employee.objects.filter('select_role')
    #     print(employee_obj)
    def post(self, request, *args, **kwargs):
        # a = Employee.objects.all()
        # for i in a:
        #     print(i.select_role)
        # print(a)
        
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        # print(form)
        form.save()
        messages.success(request=self.request, message="successfully create")
        super().form_valid(form)
        return redirect('employee_list')

    # def form_invalid(self, form):
    #     messages.error(self.request,"nciusbfvsb")
    #     return super().form_invalid(form)

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
        return redirect('employee_list')