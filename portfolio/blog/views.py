from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .models import Profile
from subprocess import run, PIPE
import sys

# Create your views here.
def home(request):
    return render(request, 'blog/base.html')

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'blog/projects.html', context)

def resume(request):
    return render(request, 'blog/resume.html')

def dmoj(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'blog/dmojprofilemaker.html', context)

def execute(request):
    info=request.POST.get("info")
    out= run([sys.executable, 'C:/Users/Nathan/Desktop/port/portfoliosite/portfolio/main.py', info], shell = False, stdout=PIPE)
    print(out)
    return dmoj(request)