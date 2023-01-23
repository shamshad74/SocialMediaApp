from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from api.models import Posts,UserProfile

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-select"})
        }

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class ProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=["user","proimage","dob"]

        widgets={
            "dob":forms.DateInput(attrs={"type":"date","class":"form-control"})
        }


