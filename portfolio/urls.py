from django.contrib import admin
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.aboutme_view, name='aboutme'),
    path('contact/', views.contact_view, name='contact'),
    path('experience/', views.experience_view, name='experience'),
]
