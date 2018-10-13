from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password,check_password
from django.http.response import HttpResponseRedirect
# Create your views here.

def index(request):

    user = request.user

    return render(request,'index.html',context={'user':user})

def registration(request):
    message = ''

    if request.method=='POST':
        login_ = request.POST['login']
        password_ = request.POST['password']
        user:User = None
        created=False
        try:
            user = User.objects.get(username=login_)

        except Exception as ex:
            new_user = User.objects.create(username=login_,password=make_password(password_))
            created=True
        if created:
            return redirect('login')
        else:

            message = 'Login already exist'
            return render(request,'registration.html', context={'message':message})
    else:
        return render(request,'registration.html',context={'message':message})


def login1(request):
    if request.method=='POST':
        login_ = request.POST['login']
        password_ = request.POST['password']
        user = authenticate(request,username=login_,password=password_)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('registration')


    else:
        return render(request,'login.html')

    pass

@login_required(login_url='/login')
def chat(request):

    user = request.user

    return render(request,'chat1.html',context={'user':user})

def logout1(request):
    logout(request)
    return redirect('login')

def test_id(request,id):
    if id is None:
        id='null'
    return render(request,'test_id.html',context={'id':id})