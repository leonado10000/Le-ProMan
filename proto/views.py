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