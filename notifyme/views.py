from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def NotifyMe(request):
    return render(request, 'notifyme/home.html')

def SignUp(request):
    return render(request, 'notifyme/signup.html')

def Confirmation(request):
    return render(request, 'notifyme/confirmation.html')
