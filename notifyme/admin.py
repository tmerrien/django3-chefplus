from django.contrib import admin
from . models import MailMessage, Subscriber

# Register your models here.
admin.site.register(MailMessage)
admin.site.register(Subscriber)
