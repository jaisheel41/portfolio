# main/admin.py
from django.contrib import admin
from .models import Skill, Education, Project, Certification, Experience, Contact

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Experience)
admin.site.register(Contact)
