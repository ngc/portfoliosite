from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'blog/base.html')

def projects(request):
    return render(request, 'blog/projects.html')

def resume(request):
    return render(request, 'blog/resume.html')

def cp(request):
    return render(request, 'blog/cp.html')
