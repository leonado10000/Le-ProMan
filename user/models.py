from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def def_img():
    return "https://static01.nyt.com/images/2021/04/30/multimedia/30xp-meme/29xp-meme-mediumSquareAt3X-v5.jpg"
    return "https://static.wikia.nocookie.net/solo-leveling/images/8/8b/Jinwoo4.jpg"

def def_course_img():
    return "https://cdn.dribbble.com/users/9853924/screenshots/19234500/media/2de3ef20f56373dc1baef595866aff42.jpg"

class profile(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE ,related_name = "fk")
    profile_img = models.CharField(max_length = 200,default = def_img)

    def __str__(self) -> str:
        return f"{self.uid}"
    def __list__(self) -> list:
        usr = User.objects.get(uid = self.uid)
        return [usr]





class Courses(models.Model):
    Course_ID = models.CharField(primary_key = True, max_length=10)
    Course_name = models.CharField(max_length=50, unique=True,default="(*_*)")
    Date_added = models.DateTimeField(auto_now=True)
    No_of_enrolment = models.IntegerField(default=0)
    Course_description = models.CharField(max_length = 1200,null=True)
    Image_link = models.CharField(max_length=150,default=def_course_img)

    def __str__(self) -> str:
        return f"{self.Course_ID} :  {self.Course_name}"
    def __list__(self) -> list:
        return [self.Course_ID,self.Course_name,self.Date_added,self.No_of_enrolment,self.Course_description,self.Image_link]



class Topics(models.Model):
    Topic_ID = models.CharField(primary_key = True, max_length=10)
    Topic_name = models.CharField(max_length=50,default="(*-*)")
    Topic_description = models.CharField(max_length=1200,null=True)
    Last_updated = models.DateTimeField(auto_now=True)
    Topic_Sources = models.CharField(max_length=1000,null=True)

    def __str__(self) -> str:
        return f"{self.Topic_ID} :  {self.Topic_name}"
    def __list__(self) -> list:
        return [self.Topic_ID,self.Topic_name,self.Topic_description,self.Last_updated]










class CTtable(models.Model):
    Course_ID = models.ForeignKey('Courses', related_name = "ct_cid", on_delete = models.CASCADE)
    Topics_IDs = models.CharField(max_length=10000,null=True)
    # Related_topic_IDs = models.CharField(max_length=10000,null=True)
    Course_rating = models.IntegerField(default=0)
    Recommended_Time = models.IntegerField(default=0)


    def __str__(self) -> str:
        return f"{self.Course_ID}"
    def __list__(self) -> list:
        return [self.Course_ID,self.Topics_IDs,self.Course_rating,self.Recommended_Time]






class Prograss(models.Model):
    User_ID = models.ForeignKey(User, related_name = "prog_uid", on_delete = models.CASCADE)
    Course_ID = models.ForeignKey('Courses', related_name = "prog_cid", on_delete = models.CASCADE)
    Completed_topic_IDs = models.CharField(max_length=1000,null=True,default = "0")
    Incompleted_topic_IDs = models.CharField(max_length=1000,null=True)
    Start_date = models.DateTimeField(auto_now=True)
    Finish_date = models.DateTimeField(auto_now=True) # if Finish date is same as Start_date // display as unfinished


    def __str__(self) -> str:
        return f"{self.User_ID} :  {self.Course_ID}"
    def __list__(self) -> list:
        return [self.User_ID,self.Course_ID,self.Completed_topic_IDs,self.Incompleted_topic_IDs,self.Start_date,self.Finish_date]