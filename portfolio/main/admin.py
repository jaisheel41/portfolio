# main/admin.py
from django.contrib import admin
from .models import Skill, Education, Project, Certification, Contact

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Contact)
