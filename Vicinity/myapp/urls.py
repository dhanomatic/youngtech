from django.urls import path
from .views import Home, UserCreateView, DepartmentListView, DepartmentCreateView
from myapp import views

urlpatterns = [
    path('', Home.as_view()),
    path('login/', views.loginpage, name='login'),
    path('user/', UserCreateView.as_view(), name='user-reg'),
    path('dept/', DepartmentCreateView.as_view(), name='dept-reg'),
    path('list/', DepartmentListView.as_view()),
    path('approval/<int:did>', views.DepartmentApprove),
    path('rejection/<int:did>', views.DepartmentReject),
]