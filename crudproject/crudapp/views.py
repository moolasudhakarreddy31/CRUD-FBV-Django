from django.shortcuts import render,redirect
from crudapp.models import Employee
from crudapp.forms import EmployeeForm


# Create your views here.

def retrive_view(request):
    employee=Employee.objects.all()

    return render(request,'crudapp/index.html',{'employee':employee})


def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request,'crudapp/create.html',{'form':form})


def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/home')

def update_view(request):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'crudapp/update.html',{'employee':employee})
