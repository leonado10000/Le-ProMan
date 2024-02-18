from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from .models import *
#################### index####################################### 
def index(request):
	data = ""
	if request.user.is_authenticated:
		data = User.objects.get(username=request.user.username).__dict__
	return render(request, 'user/index.html', {
		'title':'index',
		'userdata' : data
		})

########### register here ##################################### 
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system #################################### 
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms################################################### 
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})










def about(request):
	return render(request, 'Aboutus/png.html')

def course_list(request):
	courseData = [x.__dict__ for x in Courses.objects.all()]
	return render(request, 'course_list/courseListPage.html' ,{
		"courseData":courseData
	})











def pprofile(request,username):
	if request.user.is_authenticated:
		try:
			userdata = User.objects.get(username=username)
			profiledata = ""
			if userdata:
				userdata = userdata.__dict__
				profiledata = profile.objects.get(uid = userdata['id'])
			
			return render(request, 'profile/profile.html' ,{
				"userdata" : userdata,
				"profiledata":profiledata
			})
		except :
			messages.info(request, "User does not exist")
			return redirect('index')
	else:
		return redirect('login')










def course(request, courseid):
	course = Courses.objects.get(Course_ID = courseid).__dict__
	topicdata = [Topics.objects.get(Topic_ID=tid).__dict__ for tid in str(CTtable.objects.get(Course_ID=course['Course_ID']).__dict__['Topics_IDs']).split(',')]
	enrollementStatus = False
	progressData = ""





	if request.user.is_authenticated:
		# print(request.user.id)
		progressDatas = [x.__dict__ for x in Prograss.objects.filter(User_ID = 1)]
		for val in progressDatas:
			# print(val,course)
			if str(val['Course_ID_id']) == course['Course_ID']:
				progressData = val
				enrollementStatus = True


				# ---------------------------------------------------
				# Only if the user is logged in and enrolled in the course
				# Following id to save the progress
				if request.method == "POST":
					print(request.POST)
					print(topicdata)





	# print(course['Image_link'])
	return render(request, 'courses/general.html', {
		"courseData":course,
		"topicdatas_basic":topicdata,
		"topicdatas_inter":"",
		"topicdatas_adv":"",
		"isEnrolled":enrollementStatus,
		"progressData":progressData
	})

