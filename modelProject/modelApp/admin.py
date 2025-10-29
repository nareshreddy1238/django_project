from django.contrib import admin
from modelApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'salary','email']
admin.site.register(Employee, EmployeeAdmin)