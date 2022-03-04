from django.urls import path
from .views import ProductAdd,ProductList,ProductDetail,ProductUpdate

urlpatterns = [
    path('add/',ProductAdd.as_view()),
    path('list/',ProductList.as_view()),
    path('<int:pk>',ProductDetail.as_view()),
    path('update/<int:pk>',ProductUpdate.as_view()),

]