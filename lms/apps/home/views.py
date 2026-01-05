from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm

# Create your views here.

def home(request):
    return render(request,"home/index.html")

def student_registation(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"home/registration.html",{"success":"Registration has been successfully!"})
    else:
        initial_data = {"username": "", "email":"", "password1": "","password2": ""}
        form = CustomUserCreationForm(initial= initial_data)
    return render(request,"home/registration.html",{"form":form})

def student_login(request):
    if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
           user = form.get_user()
           login(request,user)
           return redirect("home")
    else:
        form = AuthenticationForm(request)  
           
    return render(request,"home/login.html",{"form":form})

def student_logout(request):
    logout(request)
    return redirect("home")

def dashboard(request):
   return render(request,"home/dashboard.html")



