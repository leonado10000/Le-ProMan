from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    login_val = "False"
    if request.method == "POST":
        Uname = request.POST["Username"]
        Pword = request.POST["password"]
        print(Uname,Pword)
        User_obj = authenticate(request, username=Uname,password=Pword)
        if User_obj is not None:
            login_val = "True"
    return render(request, "index.html" , {
        "login":login_val
    })



def coursePage(request, courseName):

    return render(request, "coursePage.html",{
        "courseName":courseName,
    })

def userPage(request, userID):

    return render(request, 'userPage.html',{
    })


def courses(request):

    return render(request, 'allCourses.html',{
        "courses":courses,
    })

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
