from django.urls import path
from photoapp.views import StudentView, StudentList, StudentSearch, StudentUpdate, StudentDelete, HomePage, EmpAdd, EmpList,EmpUpdate,EmpDetail,EmpDelete
from .import views

urlpatterns = [
    path('',HomePage.as_view()),
    path('add/',StudentView.as_view()),
    path('list/',StudentList.as_view()),
    path('detail/<int:pk>',StudentSearch.as_view()),
    path('update/<int:pk>',StudentUpdate.as_view()),
    path('delete/<int:pk>',StudentDelete.as_view()),
    path('empadd/',EmpAdd.as_view()),
    path('emplist/',EmpList.as_view()),
    path('empupdate/<int:pk>',EmpUpdate.as_view()),
    path('empdetail/<int:pk>',EmpDetail.as_view())                                          ,
    path('empdelete/<int:pk>',EmpDelete.as_view()),
]