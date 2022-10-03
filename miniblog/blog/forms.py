from django.db import models
from django.forms import ModelForm
from .models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


