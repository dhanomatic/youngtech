from django.shortcuts import render
from .models import Product
from django.views.generic import CreateView,ListView,DetailView,UpdateView

# Create your views here.

class ProductAdd(CreateView):
    model = Product
    fields = ['pname','qty','rate']
    success_url = '/'

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductUpdate(UpdateView):
    model = Product
    fields = ['pname','qty','rate']
    success_url = '/'