from django.shortcuts import render
from user.models import *
# from models import job_opening
# Create your views here.

def applicantdashboard(request):    
    return render(request,'applicantdashboard.html')

def joblist(request):
    tag = request.POST.get('skill')
    
    job_opening = Job_Opening.objects.filter(skill=tag)
    
  
    context = {'job_opening': job_opening}
    return render(request,'joblist.html',context)