from django.urls import path
from .views import AddHouse,ListHouse,UpdateHouse,DeleteHouse,DetailHouse

urlpatterns = [
    path('add/',AddHouse.as_view()),
    path('list/',ListHouse.as_view()),
    path('update/<int:pk>',UpdateHouse.as_view()),
    path('detail/<int:pk>',DetailHouse.as_view()),
    path('delete/<int:pk>',DeleteHouse.as_view()),
]