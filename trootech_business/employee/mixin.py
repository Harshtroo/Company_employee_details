from django.core.exceptions import PermissionDenied
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Employee, Depatment

class RoleRequiredMixin:
    ''' role require class'''
    def dispatch(self, request, *args, **kwargs):
        '''dispatch method'''
        if request.user.has_access:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,"You are not Authorised.")
            return redirect('employee_list')

# class EditProfilemixin:
#     ''' edit permisions'''
#     def dispatch(self, request, *args, **kwargs):
#         '''edit dispatch'''
#         user_role = request.user.select_role.all()
#         # user_dep = [i.Depatment for i in user_role]
#         # print(user_dep)

#         if Depatment().get_all_roles():
#             print("user roel:  ",user_role[0].name)
#             if user_role[0].name == 'DEVELOPER':
#                 print("dfnvjddb")
#                 print(Depatment().get_all_roles())
#                 return super().dispatch(request, *args, **kwargs)
#             else:
#                 print("else")
#                 return super().dispatch(request, *args, **kwargs)



        # if request.user.select_role.filter(id="9").exists():
        #     return super().dispatch(request, *args, **kwargs)
        # else:
        #     print(request.user.select_role.values())
        #     messages.error(request,"You are not Authorised.")
        #     return redirect('employee_list')

        # if Employee.select_role.all():
        #     print("<<<<<<<<<<<<>>>>>>>>>>>>",Employee.select_role.all())
        #     return super().dispatch(request, *args, **kwargs)
        # if request.user.select_role.all():
        #     print(request.user.select_role.all())
        #     return super().dispatch(request, *args, **kwargs)
       