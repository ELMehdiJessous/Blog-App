from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .form import *

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['userName']
        userpassword = request.POST['userPass']
        
        if not User.objects.filter(username = username).exists():
            return render(request, "accounts/login.html",{'error':"username not exist !"})
        
        user = authenticate(request,username=username,password = userpassword)
        
        if user is None:
            return render(request, "accounts/login.html",{'error':"password incorrect !"})
        
        auth_login(request,user)
        return redirect("home")
    return render(request,"accounts/login.html")

def signup(request):
    form = signupform()
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'form':form}
    return render(request,"accounts/signup.html",context)

def logout(request):
    auth_logout(request)
    return redirect("home")