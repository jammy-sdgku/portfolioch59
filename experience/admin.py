from django.contrib import admin
from .models import Experience, Education, Certification

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date', 'order']
    list_editable = ['order']
    filter_horizontal = ['skills']
    list_filter = ['company']
    search_fields = ['company', 'position', 'description']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_date', 'end_date', 'order']
    list_editable = ['order']
    filter_horizontal = ['skills']
    search_fields = ['institution', 'degree']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['issuing_organization', 'name', 'year_certified', 'order']
    list_editable = ['order']
    filter_horizontal = ['skills']
    search_fields = ['issuing_organization', 'name']
