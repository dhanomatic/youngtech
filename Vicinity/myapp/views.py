from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import UserReg, DeptReg
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


class DepartmentCreateView(CreateView):
    model = DeptReg
    fields = '__all__'
    success_url = '/'

    def get_initial(self, *args, **kwargs):
        max_did = DeptReg.objects.aggregate(max_did=Coalesce(Max('did'), Value(0)))['max_did']
        bno = int(max_did) + 1
        initial = super(DepartmentCreateView, self).get_initial(**kwargs)
        initial['did'] = bno
        # initial['right'] = 'user'
        return initial

    def form_valid(self, form):
        post = form.save(commit=False)
        id = post.did
        n = post.username
        print(id)
        found = 0
        if DeptReg.objects.filter(username=n).exists():
            found = 1
        if found == 0:
            post.save()
            return HttpResponseRedirect('http://127.0.0.1:8000')
        else:
            return render(self.request, "DeptReg_form.html")


class DepartmentListView(ListView):
    model = DeptReg
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = DeptReg.objects.filter(status='new department')
        return context

def DepartmentApprove(request,did):
    DeptReg.objects.filter(did=did).update(status="Department")
    return redirect('/list/')

def DepartmentReject(request, did):
    DeptReg.object.filter(did=did).update(status='Reject')
    return redirect('/list')