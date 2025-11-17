from django.shortcuts import render
from .models import Experience, Education, Certification

def experience_view(request):
    experiences = Experience.objects.prefetch_related('skills').all()
    education = Education.objects.prefetch_related('skills').all()
    certifications = Certification.objects.prefetch_related('skills').all()
    
    context = {
        'experiences': experiences,
        'education': education,
        'certifications': certifications,
    }
    return render(request, 'portfolio/experience.html', context)
