from django import forms
from . models import Subscriber, MailMessage

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', ]
