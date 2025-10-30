from django.shortcuts import render

# Create your views here.
def aboutme_view(request):
    return render(request, 'portfolio/aboutme.html')

def contact_view(request):
    return render(request, 'portfolio/contact.html')

def experience_view(request):
    return render(request, 'portfolio/experience.html')