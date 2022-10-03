from django.db import models
import datetime
from django.contrib.auth.models import  User

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name




class Post(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    author = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)
    content = models.TextField(max_length=1000,default='')

    class Meta:
        ordering = ['-post_date']



    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey( User, models.SET_NULL,blank=True,null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, help_text='what are your thoughts?')

    def __str__(self):
        return self.content[:10]

    class Meta:
        ordering =['post_date']

