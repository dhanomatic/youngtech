from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import UserReg
from django.db.models.functions import Coalesce
from django.db.models import Max, Value

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class UserCreateView(CreateView):
    model = UserReg
    fields = '__all__'
    success_url = '/'

    def get_initial(self, *args, **kwargs):
        max_uid = UserReg.objects.aggregate(max_uid=Coalesce(Max('uid'), Value(0)))['max_uid']
        bno = int(max_uid) + 1
        initial = super(UserCreateView, self).get_initial(**kwargs)
        initial['uid'] = bno
        # initial['right'] = 'user'
        return initial

    def form_valid(self, form):
        post = form.save(commit=False)
        id = post.uid
        n = post.username
        print(id)
        found=0
        if UserReg.objects.filter(username=n).exists():
            found=1
        if found==0:
            post.save()
            return HttpResponseRedirect('http://127.0.0.1:8000')
        else:
            return render(self.request,"UserReg_form.html")



