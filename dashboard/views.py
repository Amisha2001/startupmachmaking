from django.shortcuts import render
from user.models import *
from django.http import HttpResponse
from django.core.mail import send_mail

def applicantdashboard(request):    
    return render(request,'applicantdashboard.html')

def joblist(request):
    tag = request.POST.get('skill')
    
    job_opening = Job_Opening.objects.filter(skill=tag)
    
  
    context = {'job_opening': job_opening}
    return render(request,'joblist.html',context)

def send_email(request):
    if request.POST:
        company_name=request.POST['company_name']
        job_desc = request.POST['job_desc']
        location = request.POST['location']
        expirence = request.POST['expirence']
        skill = request.POST['skill']
        job_id=request.POST['job_id']
        obj = application(user=request.user,job=Job_Opening.objects.get(pk=job_id))
        obj.save()
    send_mail(
        'Confirmation mail from MatchMaking',
        "|||{} ||| {} \\\ {} \\\ {} \\\ {} |||||".format(job_desc,location,expirence,skill,company_name),
        'varun.er13.6@gmail.com',
        [request.user.email],
        fail_silently=False,
    )
    return HttpResponse("hello")
