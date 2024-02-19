from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("course/<str:courseName>/", views.coursePage, name="coursePage"),
    path("user/<str:userID>", views.userPage, name="userPage"),
    path("courses/", views.courses, name="courses"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]