from django.shortcuts import render, redirect
from .models import Employee,Student,Useraccount
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


def addrecords(request):
    if request.method=="POST":
        n = request.POST.get("t1")
        p = request.POST.get("t2")
        r = Student(name=n, place=p)
        r.save()
        return redirect('/')
    else:
        return render(request,"student.html")

def adduser(request):
    if request.method=="POST":
        a = request.POST.get("t1")
        b = request.POST.get("t2")
        c = request.POST.get("t3")
        r = Useraccount(uname=a, pword=b, right=c)
        r.save()
        return redirect('/')
    else:
        return render(request, "user.html")


def checklogin(request):
    if request.method=="POST":
        n = request.POST.get("t1")
        p = request.POST.get("t2")
        urec = Useraccount.objects.filter(uname=n, pword=p)
        if urec.filter(uname=n, pword=p).exists():
            for i in urec:
                r=i.right
            request.session['un']=n
            request.session['pw']=p
            request.session['r']=r
            if r=="A":
                return render(request,"AdminPage.html")
            elif r=='U':
                return render(request, "UserPage.html")
            else:
                return render(request, "EmpPage.html")
    else:
        return render(request, "login.html")


