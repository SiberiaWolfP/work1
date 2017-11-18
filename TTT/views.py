from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from TTT.models import Baike

# Create your views here.
from django.views.decorators.csrf import csrf_protect


def register_view(req):

    if req.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    if req.method=='POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = UserCreationForm()

    return render(req,'register.html',{'form':form})

@csrf_protect
def login_view(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(req,username=username,password=password)
    if req.user.is_authenticated():
        return HttpResponseRedirect('/logged/')
    elif user is not None:
        auth.login(req,user)
        return HttpResponseRedirect('/index/')
    return render(req,'login.html')

def logout_view(req):
    auth.logout(req)
    return HttpResponseRedirect('/login')

@login_required
def index(req):
    passages = Baike.objects.all()
    return render(req,'index.html',{'passages':passages})

def logged(req):
    return render(req,'logged.html')

def main(req):
    return render(req,'main.html')
















































































































































































