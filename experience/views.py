from django.shortcuts import render
from .models import Experience, Education, Certification

def experience_view(request):
    experiences = Experience.objects.prefetch_related('skills').all()
    context = {
        'experiences': experiences,
    }
    return render(request, 'portfolio/experience.html', context)

def education_view(request):
    education = Education.objects.prefetch_related('skills').all()
    context = {
        'education': education,
    }
    return render(request, 'portfolio/education.html', context)

def certification_view(request):
    certifications = Certification.objects.prefetch_related('skills').all()
    context = {
        'certifications': certifications,
    }
    return render(request, 'portfolio/certifications.html', context)