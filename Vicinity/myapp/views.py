from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import UserReg, DeptReg, Post, Vote, Message, Complaints
from django.db.models.functions import Coalesce
from django.db.models import Max, Value, F
from .form import PostForm, MessageForm, ComplaintForm



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
        found = 0
        if UserReg.objects.filter(username=n).exists():
            found = 1
        if found == 0:
            post.save()
            return HttpResponseRedirect('http://127.0.0.1:8000')
        else:
            return render(self.request, "UserReg_form.html")


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


def DepartmentApprove(request, did):
    DeptReg.objects.filter(did=did).update(status="Department")
    return redirect('/list/')


def DepartmentReject(request, did):
    DeptReg.objects.filter(did=did).update(status='Reject')
    return redirect('/list/')



def loginpage(request):
    if request.method == "POST":
        found = 0
        a = request.POST.get("t1")
        b = request.POST.get("t2")
        drec = DeptReg.objects.filter(username=a, password=b)
        if drec.filter(username=a, password=b).exists():
            found = 1
            for i in drec:
                status = i.status
                id = i.did
                panchayath = i.panchayath
                request.session['uname'] = a
                request.session['pwd'] = b
                request.session['ids'] = id
                request.session['right'] = status
                request.session['panchayath'] = panchayath
                if status == 'new department':
                    return HttpResponse('Your Application is under processing')
                elif status == 'Department':
                    form = DeptReg.objects.filter(username=request.session['uname'])
                    context={'form':form}
                    return redirect('/displaydept/', context)
                elif status == 'A':
                    return render(request, "adminhome.html")
                else:
                    return HttpResponse('Your application is rejected')

        if found == 0:
            urec = UserReg.objects.filter(username=a, password=b)
            if urec.filter(username=a, password=b).exists():
                for i in urec:
                    id = i.uid
                    panchayath = i.panchayath
                    request.session['uname'] = a
                    request.session['pwd'] = b
                    request.session['id'] = id
                    request.session['panchayath'] = panchayath
                    return redirect('/display/')
            else:
                return HttpResponse("user doest exist")

    return render(request, 'login.html')


def logoutpage(request):
    return render(request, 'home.html')

def changePasswordUser(request):
    if request.method == 'POST':
        flag=0
        a = request.POST.get('t1')
        b = request.POST.get('t2')
        c = request.POST.get('t3')
        urec=UserReg.objects.filter(username=request.session['uname'], password=a)
        if urec.filter(username=request.session['uname'], password=a).exists():
            flag==1
            if b==c:
                UserReg.objects.filter(username=request.session['uname'], password=a).update(password=b)
                return redirect("/login/")
            else:
                return HttpResponse('Password miss match')
        if flag==0:
            drec=DeptReg.objects.filter(username=request.session['uname'], password=a)
            if drec.filter(username=request.session['uname'], password=a).exists():
                if b==c:
                    DeptReg.objects.filter(username=request.session['uname'], password=a).update(password=b)
                    return redirect("/login/")
                else:
                    return HttpResponse('Password miss match')
    else:
        return render(request, "changepassword.html")



def post(request):
    prec = UserReg.objects.filter(username=request.session['uname'])
    if prec.filter(username=request.session['uname']).exists():
            if request.method == "POST":
                form = PostForm(request.POST)

                if form.is_valid():
                    try:
                        form.save()
                    except:
                        pass

            else:
                form = PostForm

            return render(request, 'post.html', {'form': form})
    else:
        return HttpResponse('You are not logged in')



def postdept(request):
    pdrec = DeptReg.objects.filter(username=request.session['uname'])
    if pdrec.filter(username=request.session['uname']).exists():
            if request.method == "POST":
                form = PostForm(request.POST)

                if form.is_valid():
                    try:
                        form.save()
                    except:
                        pass

            else:
                form = PostForm

            return render(request, 'postdept.html', {'form': form})
    else:
        return HttpResponse('You are not logged in')

def displayPost(request):
    post = Post.objects.all()
    return render(request, "userhome.html", {"post":post})

def displayPostDept(request):
    post = Post.objects.all()
    return render(request, "depthome.html", {"post":post})

def upvote(request, postid):
    # like = Post.objects.geupvote)
    # like = like + 1

    uprec = Vote.objects.filter(uid=request.session['ids'], postid=postid)
    if uprec.filter(uid=request.session['ids'], postid=postid).exists():
        upr = Vote.objects.all()
        if upr.filter(upvotestatus=1, downvotestatus=0):
            return redirect('/userhome/')
        elif upr.filter(upvotestatus=0, downvotestatus=1):
            Post.objects.filter(postid=postid).update(downvote=F('downvote') - 1)
            Post.objects.filter(postid=postid).update(upvote=F('upvote') + 1)
    else:
        Post.objects.filter(postid=postid).update(upvote=F('upvote') + 1)
    # Post.objects.filter(creator=request.session['uname'], creatorid=request.session['id'])
    # Vote.objects.filter(creatorid=request.session['id']).update(upvotestatus=1)
    return redirect('/display/')


def downvote(request, postid):
    dnrec = Vote.objects.filter(uid=request.session['ids'], postid=postid)
    if dnrec.filter(uid=request.session['ids'], postid=postid).exists():
        dpr = Vote.objects.all()
        if dpr.filter(upvotestatus=0, downvotestatus=1):
            return redirect('/userhome/')
        elif upr.filter(upvotestatus=1, downvotestatus=0):
            Post.objects.filter(postid=postid).update(upvote=F('upvote') - 1)
            Post.objects.filter(postid=postid).update(downvote=F('downvote') + 1)

    else:
        Post.objects.filter(postid=postid).update(downvote=F('upvote') + 1)
    # Post.objects.filter(creator=request.session['uname'], creatorid=request.session['id'])
    # Vote.objects.filter(creatorid=request.session['id']).update(upvotestatus=1)
    return redirect('/display/')


def message(request):
    mrec = UserReg.objects.filter(username=request.session['uname'])
    if mrec.filter(username=request.session['uname']).exists():
        if request.method == "POST":
            form = MessageForm(request.POST)

            if form.is_valid():
                try:
                    form.save()
                except:
                    pass

        else:
            form = MessageForm

        return render(request, 'message.html', {'form': form})


def neighbours(request):
    nbrec = UserReg.objects.filter(username=request.session['uname'])
    if nbrec.filter(username=request.session['uname']).exists():

        nrec = UserReg.objects.filter(panchayath=request.session['panchayath'])
        return render(request, 'neighbours.html', {'nrec':nrec})
    else:
        return HttpResponse('You are not logged in')


def complaints(request):
    crec = UserReg.objects.filter(username=request.session['uname'])
    if crec.filter(username=request.session['uname']).exists():
            if request.method == "POST":
                form = ComplaintForm(request.POST)

                if form.is_valid():
                    try:
                        form.save()
                    except:
                        pass

            else:
                form = ComplaintForm

            return render(request, 'complaints.html', {'form': form})
    else:
        return HttpResponse('You are not logged in')


def complaintList(request):
    clrec = DeptReg.objects.filter(username=request.session['uname'])
    if clrec.filter(username=request.session['uname']).exists():

        crec = Complaints.objects.filter(panchayath=request.session['panchayath'])
        return render(request, 'complaintlist.html', {'crec': crec})
    else:
        return HttpResponse('You are not logged in')


def settings(request):
    return render(request, 'settings.html')