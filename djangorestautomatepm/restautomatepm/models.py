from django.db import models

class Projects(models.Model): 
    name = models.TextField()
    description = models.TextField()
    complete = models.BooleanField()
    status = models.BooleanField()
    lastupdated = models.DateField()
    company = models.TextField() 

class Phases(models.Model): 
    name = models.TextField()
    description = models.TextField()
    start = models.DateField()
    end = models.DateField() 
    complete = models.BooleanField()
    active = models.BooleanField()
    lastupdated = models.DateField()
    projectId: models.IntegerField()
    
class Log(models.Model):
    description = models.TextField()
    notes = models.TextField()
    timestamp = models.DateField()
    projectId = models.IntegerField() 

# Think about adding meta data if necessary 
