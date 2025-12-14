from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login,logout as auth_logout, update_session_auth_hash
from .forms import *
from .models import *

# Create your views here.

@login_required
def home(request):
    posts = Posts.objects.all()
    form = FormPosts()
    if request.method == "POST":
        form = FormPosts(request.POST)
        if form.is_valid():
            y = form.save(commit=False)
            y.user = request.user
            y.save()
            form.save_m2m()
            return redirect("home")
    context = {'form':form,'posts':posts}
    return render(request,"coreApp/home.html",context)

@login_required
def change_name(request):
    posts = Posts.objects.filter(user = request.user).all()
    if request.method == 'POST':
        newName = request.POST['newName']
        newPassword = request.POST['newPassword']
        user = request.user
        
        if newName:
            if User.objects.filter(username = newName).exists():
                return render(request,"coreApp/profile.html",{'error':'username already exists!'})
            else:
                user.username = newName
                
        if newPassword:
            user.set_password(newPassword)
            update_session_auth_hash(request,user)
            
        user.save()
        return redirect("change_name")
    context = {'posts':posts}
    return render (request,"coreApp/profile.html",context)

def delete_post (reqeust,id_post):
    current_user = reqeust.user
    post = Posts.objects.filter(user = current_user).get(id = id_post)
    post.delete()
    return redirect("change_name")
    
def add_like(request,id_post):
    post = Posts.objects.get(id = id_post)
    user = request.user
    if request.method == 'POST':
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
    return redirect("home")