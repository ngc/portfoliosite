from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    body = models.TextField()
    githubLink = models.CharField(max_length=250, blank=True)
    otherLink = models.CharField(max_length=250, blank=True)
    otherLinkName = models.CharField(max_length=250, blank=True)
    imgCode = models.CharField(max_length=250, blank=True)
    order = models.IntegerField()
    def __str__(self):
        return self.title

class LastFMGraph(models.Model):
    picture = models.ImageField(default='default.png', blank=True)
    title = models.CharField(max_length=30, default='MASTER', blank=True)
    user1 = models.CharField(max_length=100, null=True)
    user2 = models.CharField(max_length=100, null=True)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default='default.png', blank=True)