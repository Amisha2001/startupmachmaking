from django.shortcuts import render
from user.models import *
from django.http import HttpResponse
from django.core.mail import send_mail

def applicantdashboard(request):    
    return render(request,'applicantdashboard.html')

def joblist(request):
    tag = request.POST.get('skill')
    job_opening = Job_Opening.objects.filter(title=tag)
    context = {'job_opening': job_opening}
    return render(request,'joblist.html',context)

def jobpost(request, slug):
    job = Job_Opening.objects.get(slug=slug)
    context = {
        'job':job
    }
    return render(request, 'jobpost.html', context)

def send_email(request):
    if request.POST:
        company_id=request.POST['company_id']
        job_id=request.POST['job_id']
        obj = application(user=request.user,job=Job_Opening.objects.get(pk=job_id))
        obj.save()
        job_details = Job_Opening.objects.get(pk=job_id)
        company_details = Company.objects.get(pk=company_id)
        send_mail(
            'Confirmation mail from MatchMaking',
            "|||{} ||| {} \\\ {} \\\ {} \\\  |||||".format(job_details.jobdesc,job_details.experience,job_details.skills,company_details.company_name),
            'startupmatchmaking@gmail.com',
            ['arjunarora2324@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("Confirmation email sent by StartUp MatchMaking")

    return HttpResponse("some error occured")
