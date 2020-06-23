from rest_framework import serializers
from restautomatepm.models import Projects, Phases, Log

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Projects 
        fields = ['id', 'name', 'complete', 'status', 'lastupdated']
class PhasesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Phases
        fields = ['id', 'name', 'complete', 'active', 'lastupdated', 'start', 'end', 'projectId']

class LogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Log
        fields = ['id', 'description', 'notes', 'timestamp', 'projectId']
