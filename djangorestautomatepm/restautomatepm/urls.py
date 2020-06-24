from django.urls import path
from restautomatepm import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()), 
    path('phases/', views.PhasesList.as_view()), 
    path('log/', views.LogList.as_view()), 
    path('projects/create/', views.CreateProject.as_view()), 
    path('projects/update/<int:pk>', views.UpdateProject.as_view()), 
    path('projects/delete/<int:pk>', views.DeleteProject.as_view()),
    path('phases/create/', views.CreatePhase.as_view()), 
    path('phases/update/<int:pk>', views.UpdatePhase.as_view()), 
    path('phases/delete/<int:pk>', views.DeletePhase.as_view()), 
    path('log/create/', views.CreateLogEntry.as_view())
]