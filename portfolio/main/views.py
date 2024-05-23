# main/views.py

from django.shortcuts import render
from .models import Skill, Education, Project, Certification

def home(request):
    return render(request, 'home.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def education(request):
    education = Education.objects.all()
    return render(request, 'education.html', {'education': education})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications.html', {'certifications': certifications})

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
    return render(request, 'contact.html')
