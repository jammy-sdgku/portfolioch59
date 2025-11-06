from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='projects/')
    repository = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, related_name='projects')

    def __str__(self):
        return f'{self.name} --({self.year})'