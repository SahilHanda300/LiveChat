from LiveChat.models import SupportForm
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name"]

class EditProfile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=["username","first_name","last_name"]

