from django.shortcuts import render
from user.models import *
# from models import job_opening
# Create your views here.

def applicantdashboard(request):    
    return render(request,'applicantdashboard.html')

def joblist(request):
    skill = request.POST.get('skill')
    # data = Job_Opening.objects.find(user_job_opening.find({"skill":skill}))
    data = Company.objects.get({'company_desc':'m'})

    return render(request,'joblist.html',{"data": data})
