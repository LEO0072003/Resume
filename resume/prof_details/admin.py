from django.contrib import admin
from .models import Profile, Academics, Certifications, WorkExperiences
# Register your models here.

admin.site.register(Profile)
admin.site.register(Academics)
admin.site.register(Certifications)
admin.site.register(WorkExperiences)
