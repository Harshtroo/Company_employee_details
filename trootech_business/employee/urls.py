from django.urls import path
from employee import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('employee_list/',views.EmployeeList.as_view(),name = 'employee_list'),
    path('add_employee/',views.CreateEmployee.as_view(),name ="add_employee"),
    path('employee_edit/<int:pk>/',views.EmployeeEditForm.as_view(),name='employee_edit'),
    path('employee_delete/<int:pk>/',views.EmployeeDelete.as_view(),name="employee_delete"),
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name="email_input.html",success_url ='/'),name ="change_password"),
    # path('input_email/',views.InputEmail.as_view(),name="input_email"),   
    path('send_email/',views.SendEmail.as_view(),name="send_email")
]
