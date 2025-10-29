from django.shortcuts import render
from modelApp.models import Employee

def employeedata(request):
    employees = Employee.objects.all()
    empDict = {'employees': employees}
    return render(request, 'emp.html', empDict)