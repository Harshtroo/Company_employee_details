from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import EmployeeForm,EmployeeEdit,SendEmail
from .models import Employee
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView,View,FormView
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse,reverse_lazy
from .mixin import RoleRequiredMixin,CustomePermissions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User, Permission
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import uuid
from django.contrib.auth import views as auth_views


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

# @method_decorator(login_required(login_url="/login/"), name='dispatch')
class EmployeeList(LoginRequiredMixin,ListView):
    ''' show employee list'''
    template_name = 'employee_list.html'
    model = Employee
    queryset = Employee.objects.filter(is_deleted = False)
    context_object_name = 'employee'
    permission_required = {
        "GET": ["employee.view_depatment"],
    }

class CreateEmployee(RoleRequiredMixin, CreateView):
    '''employee create'''
    model = Employee
    form_class = EmployeeForm
    template_name = 'add_employee.html'

    def form_valid(self, form):
        ''' create employee form valid or not.'''
        # user_form = self.form_class(self.request.POST or None)
        user = form.save(commit=False)
        user.save()
        for i in user.select_role.all():
            group = Group.objects.get(name = i.name)
            user.groups.add(group.id)
        messages.success(request=self.request, message="successfully create")
        super().form_valid(form)
        return redirect('employee_list')

    def get_success_url(self):
        ''''creae employee form and redirect url'''
        return reverse_lazy('employee_list')

class EmployeeEditForm(LoginRequiredMixin,CustomePermissions,UpdateView):
    '''employee edit form class'''
    template_name ='employee_edit.html'
    form_class = EmployeeEdit
    model = Employee
    success_url = reverse_lazy('employee_list')
    permission_required = {
        "GET": ["employee.change_depatment",],
        "POST":["employee.change_depSendEmailatment",]
    }
    # permission_required = ['employee.change_depatment','employee.add_depatment']

    def get(self,request,*args,**kwagrs):
        if request.user.id == kwagrs.get('pk') or request.user.has_access:
            return super().get(request,*args,**kwagrs)
        messages.error(self.request, message="No Permission.")
        return redirect(reverse("employee_list"))

    def form_valid(self, form):
        user_role = form.cleaned_data['select_role']
        user = Employee.objects.get(email=form.cleaned_data.get('email'))
        user.groups.clear()
        for i in user_role:
            group = Group.objects.get(name = i)
            user.groups.add(group.id)
        messages.success(request=self.request, message="Successfully updated.")
        return super(EmployeeEditForm, self).form_valid(form)

    def handle_no_permission(self):
        # add custom message
        messages.error(self.request, 'You have no permission')
        return redirect('employee_list')

class EmployeeDelete(CustomePermissions,View):
    '''employee delete class'''
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')
    permission_required = {
        "GET": ["employee.delete_depatment",],
        "POST":["employee.delete_depatment",]
    }

    def post(self, request, *args, **kwargs):
        ''''employee delete post method'''
        employee = Employee.objects.get(id=kwargs['pk'])
        employee.is_deleted = True
        employee.save()
        messages.success(request=self.request, message="successfully Deleted.")
        return HttpResponseRedirect(self.success_url)
    def handle_no_permission(self):
        # add custom message
        messages.error(self.request, 'You have no permission')
        return redirect('employee_list')

class ChangePassword(TemplateView):
    template_name = 'change_password.html'
    # form_class = SendEmail

    def get(self, request, *args, **kwargs):
        return render('change_password.html')

class InputEmail(View):
    ''' send email '''
    template_name = 'email_input.html'

    def get(self,request,*args,**kwargs):
        # uniquu_id = uuid.uuid4()
        # print(uniquu_id)
        print("bvfbbf",request.GET)
        
        return render(request, "email_input.html")

class Email(View):

    def post(self,request):
        uniquu_id = uuid.uuid4()
        # print(uniquu_id)
        print("form",request.GET)
        send_mail(
            'chnage your password ',
            " ",
            settings.EMAIL_HOST_USER,
            ['vekariyaharsh2412@gmail.com'],
            fail_silently= True,
            html_message = render_to_string('change_password.html',{'uuid': uniquu_id, "token": "token"})
        )
        messages.success(request= self.request, message="Email successfully sent")
        return redirect('login')

class PasswordReset(auth_views.PasswordResetConfirmView):
    def get_user(self, uidb64):
        # token_generator = activation_token
        pass