from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("course/<str:courseName>/", views.coursePage, name="coursePage"),
    path("user/<str:userID>", views.userPage, name="userPage"),
    path("courses/", views.courses, name="courses"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('retrieve_courses/', views.retrieve_course_data, name='retrieve_courses'),
    path('user_profile/<str:user_id>/', views.user_profile_with_progress, name='user_profile_with_progress'),
    path('course_topics/', views.retrieve_course_data, name='retrieve_course_data'),
    path('course_topics/<str:selected_course_id>/', views.course_topics, name='course_topics'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


