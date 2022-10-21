from django.shortcuts import render,redirect

# Create your views here.
from django.conf import settings
from .forms import MarketingPreferenceForm
from django.http import HttpResponse
from django.views.generic import UpdateView,View
from .models import  MarketingPreference
from django.contrib.messages.views import SuccessMessageMixin
from .utils import MailChimp

MAILCHIMP_API_KEY = getattr(settings, "MAILCHIMP_API_KEY", None)
MAILCHIMP_DATA_CENTER = getattr(settings, "MAILCHIMP_DATA_CENTER", None)
MAILCHIMP_MAIL_LIST_ID = getattr(settings, "MAILCHIMP_MAIL_LIST_ID", None)


class MarketingPreferenceUpdateView(SuccessMessageMixin,UpdateView):
    form_class = MarketingPreferenceForm
    template = 'marketing/marketingpreference_form.html'
    success_url = '/settings/email'
    success_message = 'Your email preferences have been updated. Thank you.'

    def dispatch(self,*args,**kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return redirect('/login/?next=/settings/email/')
        return super(MarketingPreferenceUpdateView, self).dispatch(*args, **kwargs)


    def get_object(self):
        user = self.request.user
        obj, create = MarketingPreference.objects.get_or_create(user=user)
        return obj

    def get_context_data(self,*args, **kwargs):
        context = super(MarketingPreferenceUpdateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Update email preference'
        return context


class MailChimpWebhookView(View):

    def post(self,request,*args,**kwargs):
        data = self.request.POST
        list_id = data.get('data[list_id]')
        if str(list_id) == str(MAILCHIMP_MAIL_LIST_ID):
            email = data.get('data[merges][EMAIL]')
            hook_type = data.get('type')
            response_status, response = MailChimp().check_subscription_status(email)
            print(response)
            sub_status = response['status']
            if sub_status == 'subscribed':
                qs = MarketingPreference.filter(user__email__iexact=email)
                qs.update(subscribed=True, mailchimp_subscribed=True,mailchimp_msg=str(data))

            elif sub_status == 'unsubscribed':
                qs = MarketingPreference.filter(user__email__iexact=email)
                qs.update(subscribed=False, mailchimp_subscribed=False,mailchimp_msg=str(data))

        return HttpResponse("Thank you", status=200)

