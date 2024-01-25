from django.db import models

# Create your models here.

class User(models.Model):
    User_ID = models.CharField(primary_key = True,max_length = 10)
    Name = models.CharField(max_length = 100)
    # Date = models.DateTimeField(auto_now = True, auto_now_add = True)

    def __str__(self) -> str:
        return f"{self.User_ID} :  {self.Name}"


class Courses(models.Model):
    Course_ID = models.CharField(primary_key = True, max_length=10)
    Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.Course_ID} :  {self.Name}"
    def __list__(self) -> list:
        return [self.Course_ID,self.Name]

class Topics(models.Model):
    Topic_ID = models.CharField(primary_key = True, max_length=10)
    Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.Topic_ID} :  {self.Name}"
    def __list__(self) -> list:
        return [self.Topic_ID,self.Name]


class CTtable(models.Model):
    Course_ID = models.ForeignKey('Courses', related_name = "ct_cid", on_delete = models.CASCADE)
    Topics = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return f"{self.Course_ID} :  {self.Topics}"
    def __list__(self) -> list:
        return [self.Course_ID,self.Topics]

class Prograss(models.Model):
    User_ID = models.ForeignKey("User", related_name = "prog_uid", on_delete = models.CASCADE)
    Course_ID = models.ForeignKey('Courses', related_name = "prog_cid", on_delete = models.CASCADE)
    PrograssBar = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.User_ID} :  {self.Course_ID} :==> {self.PrograssBar}"