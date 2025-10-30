from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.projects_view, name='projects'),
]
