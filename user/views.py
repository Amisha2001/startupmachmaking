from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Portfolio, Resume, Skill, Job, Education, Accomplishments, Company


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
                comp_name = request.POST['comp_name']
                comp_desc = request.POST['comp_desc']
                comp_logo = request.POST['comp_logo']
                comp_website = request.POST['comp_website']
                new_company = Company(user=request.user, company_name=comp_name, company_desc=comp_desc, company_logo=comp_logo, company_website=comp_website)
                new_company.save()
                return redirect('account')
            
            try:
                company = Company.objects.get(user=request.user)
                context = {'company':company}
            except:
                context = {}
    
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