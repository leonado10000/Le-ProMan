from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



def def_img():
    return "https://static.wikia.nocookie.net/solo-leveling/images/8/8b/Jinwoo4.jpg/revision/latest?cb=20210803222649"


# Define the User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, User_ID, Username, Name, Email, Join_Date, last_login, Login_map, User_image, password=None, **extra_fields):
        if not User_ID:
            raise ValueError('The User ID must be set')

        user = self.model(
            User_ID=User_ID,
            Username=Username,
            Name=Name,
            Email=Email,
            Join_Date=Join_Date,
            last_login=last_login,
            Login_map=Login_map,
            User_image=User_image,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, User_ID, Username, Name, Email, Join_Date, last_login, Login_map, User_image, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(User_ID, Username, Name, Email, Join_Date, last_login, Login_map, User_image, password, **extra_fields)

# Define the User model
class CustomUser(AbstractBaseUser):
    User_ID = models.CharField(primary_key=True, max_length=10)
    Username = models.CharField(max_length=100, default="(^o^)")
    Name = models.CharField(max_length=100, null=True)
    Email = models.EmailField(null=True)
    Join_Date = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    Login_map = models.CharField(max_length=10000, null=True)
    User_image = models.CharField(max_length=150, default="def_img")

    # Additional fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'User_ID'
    REQUIRED_FIELDS = ['Username', 'Name', 'Email', 'Join_Date', 'last_login', 'Login_map', 'User_image']

    def __str__(self):
        return self.User_ID
