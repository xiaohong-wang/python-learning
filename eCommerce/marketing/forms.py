from .models import MarketingPreference
from django import forms

class MarketingPreferenceForm(forms.ModelForm):

    subscribed = forms.BooleanField(label="Receive marketing email?", required=False)
    class Meta:
        model = MarketingPreference
        fields = ['subscribed']

