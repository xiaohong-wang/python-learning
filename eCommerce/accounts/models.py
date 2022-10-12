from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email, password=None, active=True, staff=False, admin=False):
        if not email:
            raise ValueError('User mush have an email address')

        email = self.normalize_email(email)
        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.active = active
        user_obj.staff = staff
        user_obj.admin = admin
        user_obj.save(using=self._db)

        return user_obj

    def create_staff(self,email, password):
        user_obj = self.create_user(email=email, password=password,active=True, staff=True, admin=False)

        return user_obj

    def create_superuser(self,email,password):
        user_obj = self.create_user(email=email, password=password,active=True, staff=True, admin=True)
        return user_obj





class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.staff

    def is_admin(self):
        return self.admin

    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email