from django.shortcuts import render
from .models import *
# Create your views here.
usr = User.objects.all()
crs = Courses.objects.all()
tpc = Topics.objects.all()
ctt = CTtable.objects.all()
prg = Prograss.objects.all()



def getTopicsByCourseID(CourseID):
    temp = []
    for i in CTtable.objects.get(Course_ID=CourseID).__list__()[1]:
        if i!=',':
            temp.append(Topics.objects.get(pk=int(i)).__list__()[1])
    return temp


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
    user = User.objects.get(pk=userID).__list__()
    progress_list = Prograss.objects.filter(User_ID=userID)
    progress = []
    for v in progress_list:
        completed = []
        notComplete = []
        tpcs = getTopicsByCourseID(v.__list__()[0])
        k = 0
        for status in v.__list__()[1]:
            if status=='1':
                completed.append(tpcs[k])
            else:
                notComplete.append(tpcs[k])
            k+=1
        progress.append([v.__list__()[0],completed,notComplete])
    print(progress)

    return render(request, 'userPage.html',{
        "userID":user[0],
        "userName":user[1],
        "prograss":progress
    })


def courses(request):
    courses = [obj.__list__() for obj in Courses.objects.all()]
    for i in range(len(courses)):
        temp = getTopicsByCourseID(courses[i][0])
        courses[i].append(temp)


    return render(request, 'allCourses.html',{
        "courses":courses,
    })

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
