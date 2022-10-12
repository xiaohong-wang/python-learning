from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from .signals import  object_viewed_signal
from .utils import get_client_ip
from accounts.signals import user_login_signal
from django.contrib.sessions.models import Session
from django.db.models.signals import post_save
# Create your models here.

User = settings.AUTH_USER_MODEL

class ObjectView(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True)
    object_id = models.PositiveIntegerField()
    content_obj = GenericForeignKey('content_type','object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s viewed on %s' %(self.content_obj,self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'



def object_viewed_receiver(sender,instance,request,*args,**kwargs):
    print("sender:",sender)
    print('instance:',instance)
    print('request',request)
    c_type = ContentType.objects.get_for_model(sender)


    new_view_obj = ObjectView.objects.create(
            user = request.user,
            ip_address = get_client_ip(request),
            content_type = c_type,
            object_id = instance.id,




    )

object_viewed_signal.connect(object_viewed_receiver)


class UserSession(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    ip_address = models.CharField(max_length=250, blank=True, null=True)
    session_key = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    ended = models.BooleanField(default=False)

    def end_session(self):
        session_key = self.session_key
        try:
            Session.objects.get(pk=session_key).delete()
            self.active = False
            self.ended = True
            self.save()

        except:
            pass
        return self.ended

def post_save_session_receiver(sender,instance, created, *args, **kwargs):
    if created:
        qs = UserSession.objects.filter(user=instance.user,active=True,ended=False).exclude(id=instance.id)
        for x in qs:
            x.end_session()

post_save.connect(post_save_session_receiver, sender=UserSession)

def user_login_reciever(sender,instance,request,*args,**kwargs):
    user = instance
    session_key = request.session.session_key
    new_user_session_obj = UserSession.objects.create(
        user = user,
        ip_address = get_client_ip(request),
        session_key = session_key
    )

user_login_signal.connect(user_login_reciever,)