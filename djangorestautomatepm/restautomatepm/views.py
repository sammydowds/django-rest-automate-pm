from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from restautomatepm.models import Projects, Phases, Log
from restautomatepm.serializers import ProjectsSerializer, PhasesSerializer, LogSerializer
from rest_framework import generics 


class ProjectList(generics.ListAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class CreateProject(generics.CreateAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class UpdateProject(generics.UpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class DeleteProject(generics.DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer