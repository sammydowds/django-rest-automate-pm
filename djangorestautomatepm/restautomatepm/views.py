from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from restautomatepm.models import Projects
from restautomatepm.serializers import ProjectsSerializer


@csrf_exempt
def projects(request): 
    if request.method == "GET": 
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST": 
        data = JSONParser().parse(request)
        serializer = ProjectsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
