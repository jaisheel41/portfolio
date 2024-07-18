# main/models.py
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='main/static/media/skills/', blank=True, null=True)

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.CharField(max_length=50, blank=True, null=True)  # Optional grade field

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='main/static/media/projects/', blank=True, null=True)

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_received = models.DateField()

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
