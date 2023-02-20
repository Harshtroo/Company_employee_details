from django.contrib import admin
from .models import  Employee,Depatment

# admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Depatment)
# # admin.site.register(Depatment)
# context['Depatment']=Depatment.objects.all().annotate(select_role_count = Depatment('select_role'))
