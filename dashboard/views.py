from django.shortcuts import render

# Create your views here.

def applicantdashboard(request):    
    return render(request,'applicantdashboard.html')

def joblist(request):
    skill = request.POST.get('skill')
    
    return render(request,'joblist.html',{"skill": skill})