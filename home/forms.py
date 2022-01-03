from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsersignForm(UserCreationForm):
      password1=forms.CharField(label="Enter password:",widget=forms.PasswordInput)
      password2=forms.CharField(label="Confirm password:",widget=forms.PasswordInput)
      class Meta:
        model=User
        fields=['username','first_name','last_name',"email"]
        labels={'email':'Email address:','first_name':'FIRST NAME :','username':'USERNAME :','last_name':'LAST NAME :'}