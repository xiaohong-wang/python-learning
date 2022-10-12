from django.contrib import admin
from .models import ObjectView,UserSession

# Register your models here.
admin.site.register(ObjectView)
admin.site.register(UserSession)