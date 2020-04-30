from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    githubLink = models.CharField(max_length=250)
    otherLink = models.CharField(max_length=250)
    otherLinkName = models.CharField(max_length=250)
    imgCode = models.CharField(max_length=250)
    order = models.IntegerField()
        def __str__(self):
        return self.title