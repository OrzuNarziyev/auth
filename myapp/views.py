from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


    context = {'form':form}
    return render(request,'registration/register.html',context=context)

def login_page(request):
    return render(request,'registration/login.html')

def logout_page(request):
    return render(request,'registration/logged_out.html')