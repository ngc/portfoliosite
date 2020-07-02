from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Profile, LastFMGraph
from subprocess import run, PIPE
import sys

# Create your views here.
def home(request):
    context = {
        'navtag': 0
    }
    return render(request, 'blog/about.html', context)

###PROJECTS######
    #All projects including the overview page, written posts
    #or the working demos themselves go under here
def projects(request):
    context = {
        'projects': Project.objects.all().order_by('order'),
        'navtag': 1
    }
    return render(request, 'blog/projects.html', context)

def lastfm(request):
    context = {
        'graph_img': LastFMGraph.objects.get(title="MASTER"),
        'navtag': 1
    }
    return render(request, 'blog/lastfmgraph.html', context)

def dmoj(request):
    context = {
        'profiles': Profile.objects.all(),
        'navtag': 1
    }
    return render(request, 'blog/dmojprofilemaker.html', context)

###END PROJECTS###

def resume(request):
    context = {
        'navtag': 2
    }
    return render(request, 'blog/resume.html', context)



def execute(request):
    info=request.POST.get("info")
    out= run([sys.executable, '/home/nathan/Development/portfoliosite/main.py', info], shell = False, stdout=PIPE)
    print(out)
    return redirect(dmoj)