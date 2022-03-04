from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to New project")

def showdata(request,x,y):
    c = x+y
    return HttpResponse(c)


