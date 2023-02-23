# from .models import Employee
import functools
# @functools(name='index')
def user_authoraice(view_func):
    # roles = [select_value['name'] for select_value in self.select_role.values('name')]
    # print(roles)
    @functools.wraps(view_func)
    def wrapper(request,*args,**kwargs):
        user_role = request.user.select_role['name']
        print(user_role)
    return wrapper
# def index(request):
#     role = request.user.select_role['name']
#     print(role)