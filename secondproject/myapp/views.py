from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to django")

def index1(request):
    a = 10
    b = 10
    c = a+b
    s = "sum" + str(c)
    return HttpResponse(s)
