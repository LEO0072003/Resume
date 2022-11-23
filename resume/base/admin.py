from django.contrib import admin
from .models import Milestones
from .models import User

# Register your models here.

admin.site.register(Milestones)
admin.site.register(User)
