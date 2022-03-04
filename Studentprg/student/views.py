from django.shortcuts import render
from .models import Student
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView,TemplateView


# Create your views here.

class StudentAdd(CreateView):
    model = Student
    fields = ['name','course']
    success_url = '/list'

class StudentList(ListView):
    model = Student

class StudentDetails(DetailView):
    model = Student

class StudentUpdate(UpdateView):
    model = Student
    fields = ['name','course']
    success_url = '/list'

class StudentDelete(DeleteView):
    model = Student
    success_url = '/list'

class HomePage(TemplateView):
    template_name = "student/homepage.html"

