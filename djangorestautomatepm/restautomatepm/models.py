from django.db import models

class Projects(models.Model): 
    name = models.TextField(blank=False)
    complete = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    lastupdated = models.DateField(blank=False)

class Phases(models.Model): 
    name = models.TextField()
    start = models.DateField()
    end = models.DateField() 
    complete = models.BooleanField()
    active = models.BooleanField()
    lastupdated = models.DateField()
    projectId = models.IntegerField(default=0)
    
class Log(models.Model):
    description = models.TextField(default='..changed not recorded', blank=False) 
    notes = models.TextField()
    timestamp = models.DateField()
    projectId = models.IntegerField(default=0) 

# Think about adding meta data if necessary 
