from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login

# Create your views here.
# def index(request):
#     login_val = "False"
#     if request.method == "POST":
#         Uname = request.POST["Username"]
#         Pword = request.POST["password"]
#         print(Uname,Pword)
#         User_obj = authenticate(request, username=Uname,password=Pword)
#         if User_obj is not None:
#             login_val = "True"
#     return render(request, "index.html" , {
#         "login":login_val
#     })

def index(request):
    data = [
        [x.__list__() for x in TrackerUser.objects.all()],
        [x.__list__() for x in Courses.objects.all()],
        [x.__list__() for x in Topics.objects.all()],
        [x.__list__() for x in CTtable.objects.all()],
        [x.__list__() for x in Progress.objects.all()]
    ]
    print(data)
    login_val = "False"
    if request.method == "POST":
        Uname = request.POST["Username"]
        Pword = request.POST["password"]
        print(Uname,Pword)
        User_obj = authenticate(request, username=Uname,password=Pword)
        if User_obj is not None:
            login_val = "True"
    return render(request, "index.html" , {
        "login":login_val,
        "usr":data[0],
        "crs":data[1],
        "tpc":data[2],
        "ctt":data[3],
        "prg":data[4]
    } )



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
