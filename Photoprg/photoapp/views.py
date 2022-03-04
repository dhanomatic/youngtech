from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from photoapp.models import Student,Employee
from photoapp.forms import StudentForm,EmpForm
# Create your views here.

class StudentView(CreateView):
    template_name = "student.html"
    form_class = StudentForm
    success_url = "success"

class StudentList(ListView):
    template_name = "studentlist.html"
    model = Student
    context_object_name = 'studentlist'


class StudentSearch(DetailView):
    model = Student
    template_name = "studentdetails.html"

class StudentUpdate(UpdateView):
    template_name = "update.html"
    form_class = StudentForm
    model = Student
    def get_success_url(self):
        return '/studentlist'

class StudentDelete(DeleteView):
    template_name = "delete.html"
    model = Student
    def get_success_url(self):
        return '/studentlist'

class HomePage(TemplateView):
    template_name = "home.html"


class EmpAdd(CreateView):
    template_name = "emp.html"
    form_class = EmpForm
    model = Employee
    success_url = "/emplist"

class EmpList(ListView):
    template_name = "emplist.html"
    model = Employee
    context_object_name = 'emplist'

class EmpDetail(DetailView):
    template_name = "empdetail.html"
    model = Employee


class EmpUpdate(UpdateView):
    template_name = "empupdate.html"
    form_class = EmpForm
    model = Employee
    def get_success_url(self):
        return "/emplist"

class EmpDelete(DeleteView):
    template_name = "empdelete.html"
    model = Employee
    def get_success_url(self):
        return "/emplist"