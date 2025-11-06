from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Create your views here.
def aboutme_view(request):
    return render(request, 'portfolio/aboutme.html')

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
        Name: {name}
        Email: {email}
        
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