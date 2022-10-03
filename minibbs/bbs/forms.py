from .models import Post,Comment
from django.contrib.auth.models import User
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email','password1','password2']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


