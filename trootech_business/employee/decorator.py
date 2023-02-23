from  django.http import HttpResponseRedirect
from  django.core.exceptions import PermissionDenied
from django.urls import reverse
print("fndhbvhydvs")
def role_required(allowed_roles=[]):
    def decorators(view_func):
        def wrap(request,*args,**kwargs):
            if request.user.select_role['name'] in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect(reverse('employee_list'))
        return wrap
    return decorators
