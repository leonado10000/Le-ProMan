from django.shortcuts import render
from .models import *
# Create your views here.
usr = User.objects.all()
crs = Courses.objects.all()
tpc = Topics.objects.all()
ctt = CTtable.objects.all()
prg = Prograss.objects.all()

def index(request):
    return render(request, "index.html" , {
        "usr" : list(usr),
        "crs" : list(crs), 
        "tpc" : list(tpc), 
        "ctt" : list(ctt),
        "prg" : list(prg)
    })

def coursePage(request, courseName):
    # courseName = "real"
    # find course by name in crs
    crs = Courses.objects.get(pk=courseName)
    courseName = crs.__str__()[3:]

    tpc = CTtable.objects.get(Course_ID=int(crs.__str__()[0]))
    topics_nums = [int(val) if val != ',' else 0 for val in tpc.__list__()[1]]
    topics = []
    for i in topics_nums:
        if i>0:
            topics.append(Topics.objects.get(pk=i).__list__()[1])

    return render(request, "coursePage.html",{
        "courseName":courseName,
        "topics":topics
    })

def userPage(request, userID):
    return render(request, 'userPage.html',{
        "UserID":userID
    })

def courses(request):
    courses = [obj.__list__() for obj in Courses.objects.all()]
    return render(request, 'allCourses.html',{
        "courses":courses
    })