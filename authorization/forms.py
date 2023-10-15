import sys

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField

sys.path.insert(1, "C:\Users\User\GymTracker\main")
from main.models import User


class SignUpForm(UserCreationForm):
    about = forms.TextInput()
    email = EmailField()

    class Meta:
        model = User
