from django.urls import path
from .views import Home, UserCreateView

urlpatterns = [
    path('', Home.as_view()),
    path('user/', UserCreateView.as_view()),
]