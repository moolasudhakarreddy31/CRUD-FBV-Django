from django.contrib import admin
from crudapp.models import Employee


# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empno','empname','empsal','empaddress']

admin.site.register(Employee,EmployeeAdmin)