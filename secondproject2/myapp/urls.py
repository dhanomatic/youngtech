from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('show/<int:x>/<int:y>',views.showdata),
]