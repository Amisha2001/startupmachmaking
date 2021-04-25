from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import *


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
                if name=="company_detail":
                    comp_name = request.POST['comp_name']
                    comp_desc = request.POST['comp_desc']
                    comp_logo = request.POST['comp_logo']
                    comp_website = request.POST['comp_website']
                    new_company = Company(user=request.user, company_name=comp_name, company_desc=comp_desc, company_logo=comp_logo, company_website=comp_website)
                    new_company.save()
                    company_id=new_company.id
                    print(company_id , "JSJDOASDFHASKDFJV")
                    return render(request, 'user/founder_dashboard.html', {'company_id':company_id})
                elif name=="founder_job_opening":
                    company_id=request.POST['company_id']
                    job_desc = request.POST['job_desc']
                    location = request.POST['location']
                    expirence = request.POST['expirence']
                    skill = request.POST['skill']
                    print(company_id)
                    job_opening = Job_Opening(company=Company.objects.get(pk=company_id) ,job_desc=job_desc, location=location, expirence=expirence, skill=skill)
                    job_opening.save()
                    return render(request, 'user/founder_dashboard.html', {'company_id':company_id})
            try:
                company = Company.objects.get(user=request.user)
                context = {'company':company}
            except:
                context = {}
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
                    return redirect('/dashboard/applicant')
    
        return render(request, 'user/account.html', context)
    return redirect('login')

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
    return redirect('account')

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