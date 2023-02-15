from django.urls import path
from employee import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('login/',views.Login.as_view(),name='login'),
    # path('logout/',views.Logout.as_view(),name='logout'),
    path('employee_list/',views.EmployeeDetails.as_view(),name = 'employee_list'),
    # path('employee_edit/',views.EmployeeEdit.as_view(),name='employee_edit'),
    path('add_employee/',views.CreateEmployee.as_view(),name ="add_employee")
]