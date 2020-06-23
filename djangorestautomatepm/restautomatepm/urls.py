from django.urls import path
from restautomatepm import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()), 
    path('projects/create/', views.CreateProject.as_view()), 
    path('projects/update/<int:pk>', views.UpdateProject.as_view()), 
    path('projects/delete/<int:pk>', views.DeleteProject.as_view()) 
]