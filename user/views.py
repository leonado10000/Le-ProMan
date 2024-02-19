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
	profileCreated = False
	profiledata = ""


	if request.user.is_authenticated:
		data = User.objects.get(username=request.user.username).__dict__
		if request.method == "POST":
			if request.POST['createProfile'] == 'Activate Profile':
				obj = profile(uid = User.objects.get(username=request.user.username))
				obj.save()
	
		# print("RUn",data['id'])
		try:
			profileCreated = True
			profiledata = profile.objects.get(uid = data['id']).__dict__

		except:
			profileCreated = False
		# print(profiledata)
	return render(request, 'user/index.html', {
		'title':'index',
		'userdata' : data,
		"profiledata":profiledata,
		"profileCreated":profileCreated
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
	for el in courseData:
		el['Course_description'] = el['Course_description'][:100]
	return render(request, 'course_list/courseListPage.html' ,{
		"courseData":courseData
	})











def pprofile(request,usernname):
	profiledata = ""
	if request.user.is_authenticated:
		# print("Working")
		# try:
			userdata = User.objects.get(username=usernname)
			profiledata = profile.objects.get(uid = userdata).__dict__
			#---------------------------------------------------
			#---------------------------------------------------
			# If the user is loggeed in bring all his progress data 
			progressData = [x.__dict__ for x in Prograss.objects.filter(User_ID = userdata)]
			if userdata:
				userdata = userdata.__dict__
			
			for prog in progressData:
				prog['coursename'] = Courses.objects.get(Course_ID = prog['Course_ID_id']).__dict__['Course_name']
				prog['percentage'] =  "%.2f" % (100*len([x for x in prog['Completed_topic_IDs'].split(',') if '0' <= x <= '9999'])/len([x for x in prog['Incompleted_topic_IDs'].split(',') if '0' <= x <= '999' ]))
			
				print([x for x in prog['Completed_topic_IDs'].split(',') if '0' <= x <= '9999'],[x for x in prog['Incompleted_topic_IDs'].split(',') if '0' <= x <= '999' ])
			return render(request, 'profile/profile.html' ,{
				"userdata" : userdata,
				"profiledata":profiledata,
				"progressData":progressData
			})
		# except :
			messages.info(request, "User does not exist")
			return redirect('index')
	else:
		return redirect('login')










def course(request, courseid):
	course = Courses.objects.get(Course_ID = courseid).__dict__
	print([tid for tid in CTtable.objects.get(Course_ID=course['Course_ID']).__dict__['Topics_IDs'].split(',') if '-10' <= tid <= '9999' ])
	topicdata = [Topics.objects.get(Topic_ID=tid).__dict__ for tid in str(CTtable.objects.get(Course_ID=course['Course_ID']).__dict__['Topics_IDs']).split(',') if '-10' <= tid <= '99999' ]
	enrollementStatus = False
	progressData = ""
	if request.user.is_authenticated:
		# ---------------------------------------------------
		# Only if the user is logged in and enrolled in the course
		# Following id to save the progress
		if request.method == "POST":
			print(request.POST)

			if request.POST.get("enroll-button", 0) == 'Enroll':
				incmplt_tpc = "".join([str(x["Topic_ID"]) + "," for x in topicdata])
				print(incmplt_tpc)
				p = Prograss(User_ID = request.user ,Course_ID = Courses.objects.get(Course_ID = courseid) ,Completed_topic_IDs = "0",Incompleted_topic_IDs=incmplt_tpc)
				print("saved")
				p.save()
		
			elif request.POST.get("save-progress-button", 0) == "SaveProgress" :
				print(request.POST.get("enroll-button", 0))
				completedTopics = ""
				for i in range(50):
					if 'on' in request.POST.get(f"topic_{i}_done", ''):
						completedTopics += str(i)+","
				
				# MyModel.objects.filter(pk=some_value).update(field1='some value')
				for prog in [x for x in Prograss.objects.filter(User_ID = request.user.id)]:
					if prog.__dict__['Course_ID_id'] == courseid:
						prog.__dict__["Completed_topic_IDs"] = completedTopics
						print(prog)
						prog.save()


		progressDatas = [x.__dict__ for x in Prograss.objects.filter(User_ID = request.user.id)]
		for val in progressDatas:
			if str(val['Course_ID_id']) == course['Course_ID']:
				progressData = val
				# print(topicdata)
				enrollementStatus = True
				for tdata in  topicdata:
					tdata["Completed"] = True if tdata['Topic_ID'] in "".join(val['Completed_topic_IDs']).split(',') else False


	return render(request, 'courses/general.html', {
		"courseData":course,
		"topicdatas_basic":topicdata,
		"topicdatas_inter":"",
		"topicdatas_adv":"",
		"isEnrolled":enrollementStatus,
		"progressData":progressData
	})

