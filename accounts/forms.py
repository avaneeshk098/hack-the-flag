from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Player


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')