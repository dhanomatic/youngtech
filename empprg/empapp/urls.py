from django.urls import path
from empapp import views

urlpatterns = [
    path('add/', views.addemp),
    path('display/',views.displayEmp),
    path('edit/<int:id>',views.editEmp),
    path('delete/<int:id>', views.deleteEmp),
    path('update/<int:id>', views.updateEmp),
]