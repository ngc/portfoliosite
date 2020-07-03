from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Profile, LastFMGraph
from subprocess import run, PIPE
from .forms import LastFMGraphForm
import sys
import os
import subprocess

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

    if request.method == 'POST':
        graph_form = LastFMGraphForm(request.POST, instance=LastFMGraph.objects.get(title="MASTER"))
        if graph_form.is_valid():
                graph_form.save()
                graph_instance = LastFMGraph.objects.get(title="MASTER")
                if(graph_instance.user2 != None):
                    process_argument = "-u " + graph_instance.user1 + "-" + graph_instance.user2
                else:
                    process_argument = "-u " + graph_instance.user1
                
                devnull = open(os.devnull, 'wb')
                subprocess.Popen(["nohup", sys.executable, '/home/nathan/Development/portfoliosite/lastfmgraph.py', process_argument])
                
    else:
        graph_form = LastFMGraphForm(instance=LastFMGraph.objects.get(title="MASTER"))

    context = {
        'graph_img': LastFMGraph.objects.get(title="MASTER"),
        'navtag': 1,
        'form': graph_form
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