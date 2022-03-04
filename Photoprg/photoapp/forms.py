from django import forms
from photoapp.models import Student,Employee

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= ['name','dob','photo']

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','job','salary','comm','dept']
