from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import logging

from projects.models import Skill
from .forms import ContactForm

# Set up logging
logger = logging.getLogger(__name__)

# Create your views here.
def aboutme_view(request):
    # Get all skills - the projects.Skill model only has: id, name, projects
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'portfolio/aboutme.html', context)

def experience_view(request):
    return render(request, 'portfolio/experience.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Compose email
        full_message = f"""
        'You have a new contact form submission:'
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        try:
            # Check if email settings are configured
            if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
                messages.error(request, 'Email configuration is incomplete.')
                return redirect('contact')
            
            send_mail(
                subject=f"Portfolio Contact: {subject}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            # Log the actual error for debugging
            logger.error(f"Email sending failed: {str(e)}")
            if settings.DEBUG:
                messages.error(request, f'Email error: {str(e)}')
            else:
                messages.error(request, 'There was an error sending your message. Please try again.')
        
        return redirect('contact')
    
    return render(request, 'portfolio/contact.html')

def contact2_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Compose email
            full_message = f"""
            'You have a new contact form submission:'
            
            Name: {name}
            Email: {email}
            Subject: {subject}
            
            Message:
            {message}
            """
            
            try:
                # Check if email settings are configured
                if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
                    messages.error(request, 'Email configuration is incomplete.')
                    return redirect('contact2')
                
                send_mail(
                    subject=f"Portfolio Contact: {subject}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact2')
                
            except Exception as e:
                # Log the actual error for debugging
                logger.error(f"Email sending failed: {str(e)}")
                if settings.DEBUG:
                    messages.error(request, f'Email error: {str(e)}')
                else:
                    messages.error(request, 'There was an error sending your message. Please try again.')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact2.html', {'form': form})

def world_clock(request):
    """Get world clock data for template context"""
    timezones = [
        {'city': 'New York', 'timezone': 'America/New_York'},
        {'city': 'London', 'timezone': 'Europe/London'},
        {'city': 'Tokyo', 'timezone': 'Asia/Tokyo'},
        {'city': 'Sydney', 'timezone': 'Australia/Sydney'},
    ]
    return {'timezones': timezones}