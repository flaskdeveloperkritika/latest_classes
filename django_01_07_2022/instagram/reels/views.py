from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def show(request):
    return HttpResponse('Hello Kritika')


def show_by_id(request, id):
    return HttpResponse(f'Hello, my number is : {id}')


def show_all(request):
    emp = {}
    # emp['name'] = Employee.objects.all()
    # emp['id'] = Employee.objects.all()
    # emp['location'] = Employee.objects.all()
    data = []
    #emp = Employee.objects.filter(id=1)
    emp = Employee.objects.all()
    for x in emp:
        # y = x.name
        data.append(x.name)
        #data.extend((x.id, x.name, x.location)) we can do this as well



    # stud = Employee.objects.all()
    # print("Myoutput", stud)
    # data = {'name': emp.name}
    #name = Employee['name']
    '''data = []
    for each in emp:
        # data.append(Employee.id)
        data.append(emp.name)
        data.append(emp.location)
    # print(emp)
    #print(name)
    print(data)
    print(emp)'''
    #print(y)
    return HttpResponse(data)
    '''name = Employee['name']
    id = Employee.id
    location = Employee.location
    data = {'name': name, 'id': id, 'location': location}
    print(data)
    return HttpResponse(data)'''

