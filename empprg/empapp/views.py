from django.shortcuts import render, redirect
from .models import Employee
from .form import EmpForm
# Create your views here.


def addemp(request):
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/display/')
            except:
                pass
    else:
        form=EmpForm()
    return render(request,"add.html",{"form":form})


def displayEmp(request):
    emp = Employee.objects.all()
    return render(request, "display.html", {"emp":emp})


def editEmp(request, id):
    emp = Employee.objects.get(id=id)
    form = EmpForm(instance=emp)
    return render(request, "edit.html",{"form":form, "id":id})

def updateEmp(request, id):
    emp = Employee.objects.get(id=id)
    form=EmpForm(request.POST, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/display/')
    return render(request, "edit.html", {"form":form,"id":id})

def deleteEmp(request,id):
    Employee.objects.get(id=id).delete()
    return redirect('/')