from django.urls import path
from .views import Home, UserCreateView, DepartmentListView, DepartmentCreateView
from myapp import views

urlpatterns = [
    path('', Home.as_view()),
    path('user/', UserCreateView.as_view()),
    path('dept/', DepartmentCreateView.as_view()),
    path('list/', DepartmentListView.as_view()),
    path('approval/<int:did>', views.DepartmentApprove),
    path('rejection/<int:did>', views.DepartmentReject),
]