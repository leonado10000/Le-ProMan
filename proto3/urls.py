from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("course/<str:courseName>/", views.coursePage, name="coursePage"),
    path("user/<str:userID>", views.userPage, name="userPage"),
    path("courses/", views.courses, name="courses"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('retrieve_courses/', views.retrieve_course_data, name='retrieve_courses'),
    path('user_profile/<str:user_id>/', views.user_profile_with_progress, name='user_profile_with_progress'),
]

