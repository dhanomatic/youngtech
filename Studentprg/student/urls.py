from django.urls import path
from .views import StudentAdd,StudentDetails,StudentList,StudentUpdate,StudentDelete,HomePage

urlpatterns = [
    path('',HomePage.as_view()),
    path('add/',StudentAdd.as_view()),
    path('list/',StudentList.as_view()),
    path('<int:pk>',StudentDetails.as_view()),
    path('update/<pk>',StudentUpdate.as_view()),
    path('delete/<pk>',StudentDelete.as_view()),
]