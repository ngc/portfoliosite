from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .models import Profile


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

def submit(request):
    info=request.POST['info']
    print("LOLOOLOLOL")
    # do something with info