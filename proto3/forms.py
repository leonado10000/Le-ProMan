from django import forms
from .models import TrackerUser

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = TrackerUser
        fields = ['Their_User_image']
