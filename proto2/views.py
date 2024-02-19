from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

def login_page(request):
    user_id = 0000
    password = "xxxx"
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = authenticate(request, User_ID=user_id, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.Username}!')
            return redirect('http://127.0.0.1:8000/')  # Replace 'your_redirect_url' with the actual URL you want to redirect to after login
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    form = AuthenticationForm()

    return render(request, 'login_page.html' , {
        "form":form,
        "data":[user_id,password]
    })  # Replace 'your_template.html' with the actual template name





# Create your views here.
def index(request):
    val = "valid"
    if request.method == "POST":
        print(request.POST)
        # user = authenticate(User_ID=request.POST["UID"], Password=request.POST["PWD"])
        user = authenticate(User_ID='rjdis', Password='B055M@n')
        
        if user is not None:
            # Authentication successful
            val = "logged in"
        else:
            val = "not login"
    
    return render(request, "index.html" ,{
        "val":val,
        "data":CustomUser.objects.all()
    })