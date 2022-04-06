from django.urls import path
from .views import Home, UserCreateView, DepartmentListView, DepartmentCreateView
from myapp import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('user/', UserCreateView.as_view(), name='user-reg'),
    path('dept/', DepartmentCreateView.as_view(), name='dept-reg'),
    path('list/', DepartmentListView.as_view()),
    path('approval/<int:did>', views.DepartmentApprove),
    path('rejection/<int:did>', views.DepartmentReject),
    path('post/', views.post, name='post'),
    path('postdept/', views.postdept, name='postdept'),
    path('display/', views.displayPost, name='display'),
    path('displaydept/', views.displayPostDept, name='displaydept'),
    path('change/', views.changePasswordUser, name='change'),
    path('upvote/<int:postid>', views.upvote, name='upvote'),
    path('downvote/<int:postid>', views.downvote, name='downvote'),
    path('message/', views.Message, name='message'),
    path('neighbours/', views.neighbours, name='neighbours'),
    path('complaints/', views.complaints, name='complaints'),
    path('complaintlist/', views.complaintList, name='complaintlist'),
    path('settings/', views.settings, name='settings')
]
