from django.shortcuts import render, redirect
from bookapp.models import UserAccount
from bookapp.forms import UserForm

# Create your views here.

def AddUser(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
            except:
                pass
        
    else:
        form= UserForm

    return render(request,'adduser.html',{'form':form})


