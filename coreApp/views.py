from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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