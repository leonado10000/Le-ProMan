# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# from django.contrib.postgres.fields import ArrayField
# from django.db import models
# import datetime
# from django import forms

# # Create your models here.

# def def_img():
#     return "https://static.wikia.nocookie.net/solo-leveling/images/8/8b/Jinwoo4.jpg/revision/latest?cb=20210803222649"




# class TrackerUser(models.Model):
#     Their_ID = models.CharField(primary_key = True,max_length = 10)
#     Their_Username = models.CharField(max_length=100,default="(^o^)")
#     Their_Name = models.CharField(max_length = 100,null=True)
#     Their_Email = models.EmailField(null=True)
#     Their_Password = models.CharField(max_length=20, default = "0000")
#     Their_Join_Date = models.DateTimeField(auto_now = True)
#     Their_last_login = models.DateTimeField(auto_now=True)
#     # Their_Login_map = models.CharField(max_length=10000,null=True)
#     Their_User_image = models.ImageField(upload_to='user_images/', default='static/images/default.png')  # ImageField for storing user images

#     def __str__(self) -> str:
#         return f"{self.Their_ID} > {self.Their_Username} =  {self.Their_Name}"
#     def __list__(self) -> list:
#         return [self.Their_ID,self.Their_Username,self.Their_Name,self.Their_Email,self.Their_Join_Date,self.Their_User_image]
#     def check_password(self,pword) -> bool:
#         return self.Their_Password == pword





# class Courses(models.Model):
#     Course_ID = models.CharField(primary_key = True, max_length=10)
#     Course_name = models.CharField(max_length=50, unique=True,default="(*_*)")
#     Date_added = models.DateTimeField(auto_now=True)
#     No_of_enrolment = models.IntegerField(default=0)
#     Course_description = models.CharField(max_length = 1200,null=True)
#     Image_link = models.CharField(max_length=150,default=def_img)

#     def __str__(self) -> str:
#         return f"{self.Course_ID} :  {self.Course_name}"
#     def __list__(self) -> list:
#         return [self.Course_ID,self.Course_name,self.Date_added,self.No_of_enrolment,self.Course_description,self.Image_link]



# class Topics(models.Model):
#     Topic_ID = models.CharField(primary_key = True, max_length=10)
#     Topic_name = models.CharField(max_length=50,default="(*-*)")
#     Topic_description = models.CharField(max_length=1200,null=True)
#     Last_updated = models.DateTimeField(auto_now=True)
    

#     def __str__(self) -> str:
#         return f"{self.Topic_ID} :  {self.Topic_name}"
#     def __list__(self) -> list:
#         return [self.Topic_ID,self.Topic_name,self.Topic_description,self.Last_updated]










# class CTtable(models.Model):
#     Course_ID = models.ForeignKey('Courses', related_name = "ct_cid", on_delete = models.CASCADE)
#     Topics_ID = models.ForeignKey('Topics', related_name = "ct_tid", on_delete = models.CASCADE, default = "1")
#     # Course_rating = models.IntegerField(default=0)
#     # Recommended_Time = models.IntegerField(default=0)
#     Topic_Sources = models.CharField(max_length=1000,null=True)
    
#     def __str__(self) -> str:
#         return f"{self.Course_ID}"
#     def __list__(self) -> list:
#         return [self.Course_ID,self.Topics_ID,self.Topic_Sources]






# class Progress(models.Model):
#     User_ID = models.ForeignKey("TrackerUser", related_name = "prog_uid", on_delete = models.CASCADE)
#     Course_ID = models.ForeignKey('Courses', related_name = "prog_cid", on_delete = models.CASCADE)
#     Completed_topics = ArrayField(models.CharField(max_length=100), default=list, blank=True)
#     Incomplete_topics = ArrayField(models.CharField(max_length=100), default=list, blank=True)
#     Start_date = models.DateTimeField(auto_now=True)
#     Finish_date = models.DateTimeField(auto_now=True) # if Finish date is same as Start_date // display as unfinished


#     def __str__(self) -> str:
#         return f"{self.User_ID} :  {self.Course_ID}"
#     def __list__(self) -> list:
#         return [self.User_ID,self.Course_ID,self.Completed_topics,self.Incomplete_topics,self.Start_date,self.Finish_date]
#     def save(self, *args, **kwargs):
#         # Increase the number of enrollments for the course
#         self.Course_ID.No_of_enrolment += 1
#         self.Course_ID.save()  # Save the course with updated enrollment count

#         super(Progress, self).save(*args, **kwargs)