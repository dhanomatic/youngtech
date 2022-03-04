from django.shortcuts import render
from .models import ContentModel,UserModel
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView

# Create your views here.

class ContentAdd(CreateView):
    model = ContentModel
    fields = ['username','title','content']
    success_url = '/'

class ContentUpdate(UpdateView):
    model = ContentModel
    fields = ['username','title','content']
    success_url = '/'

class ContentList(ListView):
    model = ContentModel

class ContentDetail(DetailView):
    model = ContentModel

class ContentDelete(DeleteView):
    model = ContentModel
    success_url = '/'




class UserAdd(CreateView):
    model = UserModel
    fields = ['domain','city','country']
    success_url = '/'

class UserList(ListView):
    model = UserModel

class UserUpdate(UpdateView):
    model = UserModel
    fields = ['domain','city','country']
    success_url = '/'

class UserDetail(DetailView):
    model = UserModel

class UserDelete(DeleteView):
    model = UserModel
    success_url = '/'


