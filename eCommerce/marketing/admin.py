from django.contrib import admin
from .models import MarketingPreference
# Register your models here.

class MarketingPrefereceAdmin(admin.ModelAdmin):
    list_display =['__str__','subscribed','mailchimp_subscribed','update']
    readonly_fields =['mailchimp_subscribed','mailchimp_msg','update']
    class Meta:
        model = MarketingPreference
        fields = ['user', 'subscribed','mailchimp_subscribed', 'mailchimp_msg','update']


admin.site.register(MarketingPreference,MarketingPrefereceAdmin)