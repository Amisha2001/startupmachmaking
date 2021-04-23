from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

# Create your views here.
def jobhome(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 10)
    page = request.GET.get('page')
    jobs = paginator.get_page(page)
    context = {
        'jobpostings': jobs
    }
    return render(request, 'job/jobhome.html', context)


def jobpost(request, slug):
    job = Job.objects.get(slug=slug)
    context = {
        'job':job
    }
    return render(request, 'job/jobpost.html', context)

# Create your views here.
