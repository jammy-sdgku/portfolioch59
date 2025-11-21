from django.contrib import admin
from django.urls import path, include
from portfolio import views
from experience.views import experience_view
from portfolio.views import education_view, certification_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.aboutme_view, name='aboutme'),
    path('contact/', views.contact_view, name='contact'),
    path('contact2/', views.contact2_view, name='contact2'),
    path('experience/', experience_view, name='experience'),
    path('education/', education_view, name='education'),
    path('certifications/', certification_view, name='certifications'),
]
