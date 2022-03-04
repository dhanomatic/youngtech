from django.urls import path
from .views import ContentAdd,ContentList,ContentDelete,ContentUpdate,ContentDetail,UserAdd,UserList,UserDetail,UserDelete,UserUpdate

urlpatterns = [
    path('add/',ContentAdd.as_view()),
    path('list/',ContentList.as_view()),
    path('<int:pk>',ContentUpdate.as_view()),
    path('delete/<int:pk>',ContentDelete.as_view()),
    path('detail/<int:pk>',ContentDetail.as_view()),
]


urlpatterns = [
    path('adduser/',UserAdd.as_view()),
    path('listuser/<int:pk>',UserList.as_view()),
    path('update/<int:pk>',UserUpdate.as_view()),
    path('detailuser/<int:pk>',UserDetail.as_view()),
    path('deleteuser/<int:pk>',UserDelete.as_view()),
]