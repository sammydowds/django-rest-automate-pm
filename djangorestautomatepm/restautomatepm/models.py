from django.db import models

class Projects(models.Model): 
    name = models.TextField(blank=False)
    complete = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    lastupdated = models.DateField(blank=False)

class Phases(models.Model): 
    name = models.TextField()
    description = models.TextField()
    start = models.DateField()
    end = models.DateField() 
    complete = models.BooleanField()
    active = models.BooleanField()
    lastupdated = models.DateField()
    projectId = models.IntegerField(null=True, blank=True)
    
class Log(models.Model):
    description = models.TextField()
    notes = models.TextField()
    timestamp = models.DateField()
    projectId = models.IntegerField() 

# Think about adding meta data if necessary 
