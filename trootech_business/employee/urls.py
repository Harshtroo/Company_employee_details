from django.urls import path
from employee import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('employee_list/',views.EmployeeList.as_view(),name = 'employee_list'),
    path('add_employee/',views.CreateEmployee.as_view(),name ="add_employee"),
    path('employee_edit/<int:e_id>',views.EmployeeEditForm.as_view(),name='employee_edit'),
    
]   