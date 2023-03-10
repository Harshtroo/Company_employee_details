from django.core.exceptions import PermissionDenied
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Employee, Depatment
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, User, Permission

class RoleRequiredMixin:
    ''' role require class'''
    def dispatch(self, request, *args, **kwargs):
        '''dispatch method'''
        if request.user.has_access:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,"You are not Authorised.")
            return redirect('employee_list')

class CustomePermissions(PermissionRequiredMixin):
    # content_type = ContentType.objects.get_for_model(Employee)
    # print(content_type)
    # post_permission = Permission.objects.filter(content_type=content_type)

    def has_permission(self):
        user_permissions = self.request.user.get_all_permissions()
        if self.request.method == "GET":
            if self.permission_required.get('GET')[0] in user_permissions:
                return True
            return False
        if self.request.method == "POST":
            if self.permission_required.get('GET')[0] in user_permissions:
                return True
            return False
        
        
        # print("kcdhfduvudfn",self.request.user.has_perms(self.permission_required))
        if self.request.user.is_authenticated and self.request.user.has_perms(self.permission_required):
            return True
        return False



