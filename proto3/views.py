from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.db.models import Count, F, FloatField, ExpressionWrapper, Subquery, OuterRef, Func, Case, When, Value
from django.db.models.functions import NullIf, Cast

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

def retrieve_course_data(request):
    # Retrieve the required fields from the Courses model
    courses_data = Courses.objects.values('Course_name', 'No_of_enrolment', 'Course_description')

    # Prepare the data to be passed to the template
    context = {'courses': courses_data}

    # Render the template with the data
    return render(request, 'course_data.html', context)


class ArrayLength(Func):
    function = 'CARDINALITY'
    template = '%(function)s(%(expressions)s)'

# from django.db.models import Case, When, Value, FloatField

def user_profile_with_progress(request, user_id):
    # Retrieve the user profile
    user_profile = TrackerUser.objects.get(Their_ID=user_id)

    # Retrieve the courses enrolled by the user along with the completion data
    courses_with_completion = Progress.objects.filter(User_ID=user_profile).annotate(
        total_topics=Count('Course_ID__ct_cid__Topics_ID', distinct=True),
        completed_topics_count=ExpressionWrapper(
            ArrayLength(F('Completed_topics')),
            output_field=FloatField()
        ),
        completion_percentage=ExpressionWrapper(
            NullIf((F('completed_topics_count') * 100) / F('total_topics'), 0),
            output_field=FloatField()
        )
    ).annotate(
        completion_percentage=Case(
            When(completion_percentage__isnull=True, then=Value(0)),
            default=F('completion_percentage'),
            output_field=FloatField()
        )
    ).values('Course_ID', 'Course_ID__Course_name', 'total_topics', 'completed_topics_count', 'completion_percentage')

    # Prepare the data to be passed to the template
    context = {
        'user_profile': user_profile,
        'courses_with_completion': courses_with_completion
    }

    # Render the template with the data
    return render(request, 'user_profile_with_progress.html', context)
