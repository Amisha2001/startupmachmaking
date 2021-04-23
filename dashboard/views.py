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
    # x = Job_Opening.objects.all().values()
    # job_details=[]
    # for job in x:
    #     job_details.append((job))

    # data=(str)(data)
    # data = data.split(",")
    # company_details=[]
    
    # for job in job_opening:
    #     company_details.append((list(Company.objects.filter(user_id=job.user_id).values())[0]))
        


    # print(data.user_id)

    # Company()
    # company_details = Company.objects.filter(user_id=data.user_id)
    print(company_details)
    context = {'job_details': job_details,'company_details':company_details}
    return render(request,'joblist.html',context)
