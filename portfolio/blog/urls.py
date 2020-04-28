from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('projects/', views.projects),
    path('resume/', views.resume),
    path('cp/', views.cp)
]