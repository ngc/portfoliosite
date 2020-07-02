from django.contrib import admin
from .models import Project, Profile, LastFMGraph

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(LastFMGraph)