from django.urls import path
from restautomatepm import views

urlpatterns = [
    path('projects/', views.projects)
]