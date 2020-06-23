from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from restautomatepm.models import Projects, Phases, Log
from restautomatepm.serializers import ProjectsSerializer, PhasesSerializer, LogSerializer
from rest_framework import generics 

# Returning lists endpoints
class ProjectList(generics.ListAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class PhasesList(generics.ListAPIView): 
    queryset = Phases.objects.all()
    serializer_class = PhasesSerializer

class LogList(generics.ListAPIView): 
    queryset = Log.objects.all()
    serializer_class = LogSerializer

# Editing/Deleting/Creating projects endpoints 
class CreateProject(generics.CreateAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class UpdateProject(generics.UpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class DeleteProject(generics.DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

# Editing/Deleting/Creating phases endpoints 
class CreatePhase(generics.CreateAPIView): 
    queryset = Phases.objects.all()
    serializer_class = PhasesSerializer

class UpdatePhase(generics.UpdateAPIView):
    queryset = Phases.objects.all()
    serializer_class = PhasesSerializer

class DeletePhase(generics.DestroyAPIView):
    queryset = Phases.objects.all()
    serializer_class = PhasesSerializer

#  Creating log entry 
class CreateLogEntry(generics.CreateAPIView): 
    queryset = Log.objects.all()
    serializer_class = LogSerializer
