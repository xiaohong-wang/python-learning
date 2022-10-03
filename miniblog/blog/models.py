from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text='Enter your bio details here.')

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user','b'
                           'io']

    def get_absolute_url(self):
        pass

class Blog(models.Model):
    post_date = models.DateField(null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['post_date']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.id)])





class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        title_len = 80
        if len(self.description)>80:
            title_string = self.description[:title_len] +"..."
        else:
            title_string = self.description

        return title_string

