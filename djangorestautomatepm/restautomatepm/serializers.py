from rest_framework import serializers
from restautomatepm.models import Projects, Phases, Log
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Projects 
        fields = ['id', 'name', 'complete', 'lastupdated', 'owner']

class PhasesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Phases
        fields = ['id', 'name', 'complete', 'active', 'lastupdated', 'start', 'end', 'projectId']

class LogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Log
        fields = ['id', 'description', 'notes', 'timestamp', 'projectId']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
    # Overriding create 
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user