from django.shortcuts import render
from .models import Project

def projects_view(request):
    project_list = Project.objects.all().order_by('-year')
    context = {
        'project_list': project_list
    }
    return render(request, 'projects/projects.html', context)