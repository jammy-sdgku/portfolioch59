from django.shortcuts import render

# Create your views here.
def projects_view(request):
    return render(request, 'projects/projects.html')