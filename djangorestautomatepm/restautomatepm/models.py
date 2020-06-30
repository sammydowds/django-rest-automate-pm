from django.db import models

class Projects(models.Model): 
    name = models.TextField(blank=False)
    complete = models.BooleanField(default=False)
    lastupdated = models.DateTimeField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE, null=True)

class Phases(models.Model): 
    name = models.TextField()
    start = models.DateField()
    end = models.DateField() 
    complete = models.BooleanField()
    active = models.BooleanField()
    lastupdated = models.DateTimeField()
    projectId = models.IntegerField(default=0)
    
class Log(models.Model):
    description = models.TextField(default='..change not recorded', blank=False) 
    notes = models.TextField()
    timestamp = models.DateTimeField()
    projectId = models.IntegerField(default=0) 

