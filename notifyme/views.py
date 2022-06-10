from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import SubscriberForm

# Create your views here
def NotifyMe(request):
    return render(request, 'notifyme/home.html')

def SignUp(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('../thankyou/')
    else:
        form = SubscriberForm()
    context = {
        'form': form,
    }
    return render(request, 'notifyme/signup.html', context)

def Confirmation(request):
    return render(request, 'notifyme/confirmation.html')

def MailCx(request):
    return render(request, 'notifyme/mailcx.html')

def Privacy(request):
    return render(request, 'notifyme/privacy.html')
