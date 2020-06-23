from django.urls import path
from restautomatepm import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()), 
    path('projects/create/', views.CreateProject.as_view()), 
    path('phases/', views.phases), 
    path('log/', views.log)
]