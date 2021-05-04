from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib import messages
from .models import *
from django.core.mail import send_mail

# Create your views here.
def account(request):
    if request.user.is_authenticated:
        try:
            resume = Resume.objects.get(user=request.user)
            skill = Skill.objects.filter(user=request.user)
            education = Education.objects.filter(user=request.user)
            job = Job.objects.filter(user=request.user)
            portfolio = Portfolio.objects.filter(user=request.user)
            accomplishments = Accomplishments.objects.filter(user=request.user)
            context = {'resume': resume, 'skills': skill, 'educations': education, 'jobs': job, 'portfolios': portfolio, 'accomps': accomplishments}
        except:
            context = {}
        if request.user.is_startup_founder:
            if request.POST:
                name = request.POST.get('name')
                if name=="app_profile":
                    applicant_id = request.POST['applicant_id']
                    
                    applicant = User.objects.get(pk=applicant_id)
                    resume = Resume.objects.get(user = applicant)
                    accomplishments = Accomplishments.objects.get(user = applicant)
                    education = Education.objects.get(user = applicant)
                    job = Job.objects.get(user = applicant)
                    skill = Skill.objects.get(user = applicant)
                    portfolio = Portfolio.objects.get(user = applicant)
                    context = {'applicant':applicant,'resume': resume, 'skill': skill, 'education': education, 'job': job, 'portfolio': portfolio, 'accomplishment': accomplishments}                    
                    return render(request,"user/profile.html",context)
                elif name=="company_detail":
                    comp_name = request.POST['comp_name']
                    comp_desc = request.POST['comp_desc']
                    comp_logo = request.POST['comp_logo']
                    comp_website = request.POST['comp_website']
                    new_company = Company(user=request.user, company_name=comp_name, company_desc=comp_desc, company_logo=comp_logo, company_website=comp_website)
                    new_company.save()
                    company_id=new_company.id
                    #print(company_id , "JSJDOASDFHASKDFJV")
                    return render(request, 'user/founder_dashboard.html', {'company_id':company_id})
                elif name=="founder_job_opening":
                    company_id=request.POST['company_id']
                    job_title = request.POST['title']
                    job_desc = request.POST['job_desc']
                    job_type = request.POST['job_type']
                    start_year = datetime.strptime(request.POST['start_year'], "%Y-%m-%d")
                    end_year = datetime.strptime(request.POST['end_year'], "%Y-%m-%d")
                    expirence = request.POST['expirence']
                    salary = request.POST['salary']
                    aboutjob = request.POST['about_job']
                    skill = request.POST['skill']
                    print(company_id)
                    job_opening = Job_Opening(company=Company.objects.get(pk=company_id) ,title = job_title,jobdesc=job_desc,jobtype= job_type,statdate= start_year,endate= end_year,experience=expirence,salary= salary,aboutjob=aboutjob,skills=skill)
                    job_opening.save()
                    #arpit(44)
                    jobs_opened=Job_Opening.objects.filter(company=company_id)
                    return render(request, 'user/founder_dashboard.html', {'job_opened':jobs_opened, 'company_id':company_id})
                elif name=="applied_appl":
                    job_id=request.POST['job_id']
                    print('aaaaaaaaaaaaaaaaaaaaa')
                    applicant_list = application.objects.filter(job=Job_Opening.objects.get(pk=job_id))
                    print('aaaaaaaaaaaaaaaaaaaaa')

                    return render(request, 'user/applicant_list.html', {'applicant_list':applicant_list,"job_id":job_id})
                
                elif name=="selection":
                    status=request.POST['status']
                    job_id=request.POST['job_id']
                    applicant_id=request.POST['applicant_id']

                    # app=application.objects.filter(user=User.objects.get(pk=applicant_id),job=Job_Opening.objects.get(pk=job_id))
                    application.objects.filter(user=User.objects.get(pk=applicant_id),job=Job_Opening.objects.get(pk=job_id)).update(status=status)
                    # app.refresh_from_db()

                    job_op=Job_Opening.objects.get(pk=job_id)

                    applicant_list = application.objects.filter(job=Job_Opening.objects.get(pk=job_id))

                    send_mail(
                        'Confirmation mail from MatchMaking',
                        "||| {} for the job{} of the company {} |||".format(status,job_op.title,job_op.company.company_name),
                        'startupmatchmaking@gmail.com',
                        ['arjunarora2324@gmail.com'],
                        fail_silently=False,
                    )
                    return render(request, 'user/applicant_list.html', {'applicant_list':applicant_list,"job_id":job_id})
                    
            try:

                company = Company.objects.get(user=request.user)
                #arpit(49,50,51)
                company_id=company.id
                jobs_opened=Job_Opening.objects.filter(company=company_id)
                context = {'company':company,'job_opened':jobs_opened,'company_id':company_id}
                return render(request, 'user/founder_dashboard.html', context)
            except:
                context = {}
                return render(request,'user/account.html',context)
                
        else:
            if request.POST:
                name = request.POST.get('name')
                print('NAME',name)
                if name == 'edu_form':
                    college = request.POST['college']
                    stream = request.POST['stream']
                    start_year = str(request.POST['start_year'])[:4]
                    end_year = str(request.POST['end_year'])[:4]
                    status = request.POST['status']
                    if status=="on":
                        status = True
                    else:
                        status = False
                    new_education = Education(user=request.user, status=status, college=college,  start_year=int(start_year), end_year=int(end_year) ,stream=stream)
                    new_education.save()
                    return redirect('account')
                elif name=='job_form':
                    profile = request.POST['profile']
                    organization = request.POST['organization']
                    location = request.POST['location']
                    job_desc = request.POST['job_desc']
                    start_year = datetime.strptime(request.POST['start_year'], "%Y-%m-%d")
                    end_year = datetime.strptime(request.POST['end_year'], "%Y-%m-%d")
                    new_job = Job(user=request.user, profile=profile, organization=organization, location=location, start_date=start_year, end_date=end_year ,job_desc=job_desc)
                    new_job.save()
                    return redirect('account')
                elif name=='port_form':
                    proj_name = request.POST['proj_name']
                    link = request.POST['link']
                    proj_desc = request.POST['proj_desc']
                    start_year = datetime.strptime(request.POST['start_year'], "%Y-%m-%d")
                    end_year = datetime.strptime(request.POST['end_year'], "%Y-%m-%d")
                    new_port = Portfolio(user=request.user, proj_name=proj_name, link=link, proj_desc=proj_desc, start_date=start_year, end_date=end_year)
                    new_port.save()
                    return redirect('account')
                elif name=='skill_form':
                    skill_name = request.POST['skill_name']
                    skill_level = request.POST['skill_level']
                    new_skill = Skill(user=request.user, skill_name=skill_name, skill_level=skill_level)
                    new_skill.save()
                    return redirect('account')
                elif name=='acomp_form':
                    desc = request.POST['desc']
                    new_acomp = Accomplishments(user=request.user,desc=desc)
                    new_acomp.save()
                    return redirect('account')
                elif name=='res_form':
                    print('entered')
                    bio = request.POST['bio']
                    avatar = request.POST['avatar']
                    ph_no = request.POST['ph_no']
                    primary_city = request.POST['pri_city']
                    secondary_city = request.POST['sec_city']
                    new_resume = Resume(user=request.user, desc=bio, avatar=avatar, phn_no=ph_no, primary_city=primary_city, secondary_city=secondary_city)
                    new_resume.save()
                    print('saved')
                    return redirect('account')  #temporary
                    #arpit(113,114,115)
                elif name=='dashboard':
                    if Resume.objects.filter(user=request.user) and  Accomplishments.objects.filter(user=request.user) and Skill.objects.filter(user=request.user) and Portfolio.objects.filter(user=request.user) and Job.objects.filter(user=request.user) and Education.objects.filter(user=request.user):
                        return redirect('/dashboard/applicant')
                    else:
                        messages.info(request,'Please fill all details to go to dashboard.')
                        return render(request,'user/account.html') 
                elif Resume.objects.filter(user=request.user) and  Accomplishments.objects.filter(user=request.user) and Skill.objects.filter(user=request.user) and Portfolio.objects.filter(user=request.user) and Job.objects.filter(user=request.user) and Education.objects.filter(user=request.user):
                    return redirect('/dashboard/applicant')
                else:
                    return render(request,'user/account.html')   
                return redirect('/dashboard/applicant')
            else:
                if Resume.objects.filter(user=request.user) and  Accomplishments.objects.filter(user=request.user) and Skill.objects.filter(user=request.user) and Portfolio.objects.filter(user=request.user) and Job.objects.filter(user=request.user) and Education.objects.filter(user=request.user):
                    return redirect('/dashboard/applicant')
                else:
                    # messages.info(request,'Please fill all details to go to dashboard.')
                    return render(request,'user/account.html')  
    return redirect('/')

def usrlogin(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('account')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('account')
        else:
            context['login_form'] = form
    else:
        form = LoginForm()
        context['login_form'] = form
    return render(request, 'user/login.html', context)

def usrlogout(request):
    logout(request)
    return redirect('/')

def signup(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('account')
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            new_account = authenticate(email=email, password=raw_pass)
            login(request, new_account)
            return redirect('account')
        else:
            context['signup_form'] = form
    else:
        form = SignupForm()
        context['signup_form'] = form
    return render(request, 'user/signup.html', context)


def profile(request):
    
    try:
        print("kkkkkkkkkkkkkkkkk")
        applicant = request.user
        print("kkkkkkkkkkkkkkkkk00000")
        resume = Resume.objects.get(user=request.user)
        skill = Skill.objects.get(user=request.user)
        education = Education.objects.get(user=request.user)
        job = Job.objects.get(user=request.user)
        portfolio = Portfolio.objects.get(user=request.user)
        accomplishments = Accomplishments.objects.get(user=request.user)
        context = {'applicant':applicant,'resume': resume, 'skills': skill, 'educations': education, 'jobs': job, 'portfolios': portfolio, 'accomplishments': accomplishments}
        print("kkkkkkkkkkkkkkkkk")
        
        return render(request, "user/profile.html", context)
    except:
        return HttpResponse("Something went wrong!!!")

