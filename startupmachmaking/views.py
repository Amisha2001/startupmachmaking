from django.shortcuts import render
from user.models import *

def home(request):
    if request.POST:
        return render(request,'landingpage.html')
    else:
        return render(request,'landingpage.html')