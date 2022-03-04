from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .form import contactform, LoginForm
# Create your views here.

def home(request):
    context = {
        'title' : "home",
        'discription': "jkhjgkvklnl"
    }
    return render(request, 'home/home.html',context)

def contact(request):
    form = contactform(request.POST or None)
    context = {
        'title': "contacts",
        'form' : form,
    }

    if form.is_valid():
        print(form.cleaned_data)

    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))

    return render(request,'contact/contact_page.html',context)


def LOGIN_PAGE(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            #redirect to success page.
            return redirect('/login')
        else:
            print('Error')

    return render(request,'registration/login_page.html', context)