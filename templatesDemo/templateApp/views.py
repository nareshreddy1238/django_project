from django.shortcuts import render

def render_first_template(request):
    myDict = {'Name': "Nani"} 
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)


def renderEmployee(request):
    emp = {'eno': 100, 'ename': 'Nani', 'esal': 1000, 'eaddr': 'Hyd'}
    return render(request, 'templatesApp/employeeTemplate.html', context=emp)