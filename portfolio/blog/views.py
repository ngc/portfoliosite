from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

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

def cp(request):
    return render(request, 'blog/cp.html')
