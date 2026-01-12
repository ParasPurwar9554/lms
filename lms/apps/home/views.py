from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.conf import settings
from django.forms.models import model_to_dict
from apps.courses.models import Course

# Create your views here.

def home(request):
    courses = Course.objects.all()
    return render(request,"home/index.html",{"courses":courses})

def course_details(request,course_slug):
    course_details = get_object_or_404(Course,slug=course_slug)
    #course_dict = model_to_dict(course_details)
    #print(course_dict)
    return render(request,"home/course_details.html",{"course_details":course_details})
    
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



