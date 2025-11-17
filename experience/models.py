from django.db import models
from projects.models import Skill

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill, related_name='experiences', blank=True)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    
    class Meta:
        ordering = ['-order', '-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill, related_name='education', blank=True)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    
    class Meta:
        ordering = ['-order', '-end_date']
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    issuing_organization = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    year_certified = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill, related_name='certifications', blank=True)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    
    class Meta:
        ordering = ['-order', '-year_certified']
    
    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"
