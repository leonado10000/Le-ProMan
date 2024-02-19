   
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
        path('', views.index, name ='index'),
        path('about', views.about, name="about"),
        path('profile/<str:usernname>',views.pprofile, name="user"),
        path('course/<str:courseid>',views.course, name="course"),
        path('courses', views.course_list, name="courses")
]