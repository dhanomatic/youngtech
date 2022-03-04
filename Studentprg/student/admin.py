from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','course')
    search_fields = ('name','course')   #to search fields

admin.site.register(Student,StudentAdmin)


