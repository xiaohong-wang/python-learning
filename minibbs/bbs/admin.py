from django.contrib import admin
from .models import Community,Comment,Post
# Register your models here.
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Post)