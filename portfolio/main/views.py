# main/views.py
from django.shortcuts import render
from .models import Skill, Education, Project, Certification, Experience

def index(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    experience = Experience.objects.all()
    return render(request, 'index.html', {
        'skills': skills,
        'education': education,
        'projects': projects,
        'certifications': certifications,
        'experience': experience,
    })
