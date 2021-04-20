from django.shortcuts import render

# Create your views here.

def applicantdashboard(request):    
    return render(request,'applicantdashboard.html')