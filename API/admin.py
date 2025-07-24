from django.contrib import admin
from .models import EmployeeDetails,Department,Skills,Training,employeeSkill
from .models import *

# Register your models here.

class employee_details_Admin(admin.ModelAdmin):
    list_display=('first_name','last_name','id','employment_id')
    list_display_links=('first_name','id')
    list_editable=('last_name','last_name')

class departments_admin(admin.ModelAdmin):
    list_display=('name_of_department','id','department_code','created_at')
    list_display_links=('id',)
    list_editable=('name_of_department',)

admin.site.register(EmployeeDetails,employee_details_Admin)

admin.site.register(Department,departments_admin)

admin.site.register(Skills)

admin.site.register(Training)
admin.site.register(employeeSkill)

