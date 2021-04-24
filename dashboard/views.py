from django.shortcuts import render
from user.models import *
# from models import job_opening
# Create your views here.

def applicantdashboard(request):    
    return render(request,'applicantdashboard.html')

def joblist(request):
    tag = request.POST.get('skill')
    
    job_opening = Job_Opening.objects.filter(skill=tag)
    # data = job_opening.split(",")
    # job_opening = Job_Opening.objects.all()
    # data=job_opening.first()
    # for i in job_opening:
    #     data=i

    # data=(str)(data)
    # data = data.split(",")
    # print(data)
    founder = []
    
    for job in job_opening:
        founder.append(job.company.company_name)
    #context = {'job_opening': job_opening}
    return render(request,'joblist.html',{'job_opening': job_opening, 'founder': founder})
