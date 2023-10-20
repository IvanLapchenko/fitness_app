import sys
from django import forms
sys.path.insert(1, "C:\\Users\\lapch\\goiteens\\Gym_Tracker_Application\\main\\")
from main.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'about', 'password']