from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserData

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserData
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserData
        fields = ("username", "email")