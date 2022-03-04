from django.shortcuts import render
from .models import HouseModel
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView

# Create your views here.

class AddHouse(CreateView):
    model = HouseModel
    fields = ['housename','housenumber']
    success_url = '/'

class ListHouse(ListView):
    model = HouseModel

class UpdateHouse(UpdateView):
    model = HouseModel
    fields = ['housename','housenumber']
    success_url = '/'

class DetailHouse(DetailView):
    model = HouseModel

class DeleteHouse(DeleteView):
    model = HouseModel
    success_url = '/'
