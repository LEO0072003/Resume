from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    USERNAME_FIELD='username'

    def __str__(self):
        if super().first_name:
            return super().get_full_name()
        else:
            return super().username



class Milestones(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    project_or_repository_link = models.URLField(null=True, blank=True)
    acknowledgement = models.ImageField(upload_to='acknowledment/', null=True, blank=True)
    project = models.ImageField(upload_to='project_images/', null=True, blank=True)
    # certifications = models.FileField(upload_to='certifications/' ,null=True, blank=True)


    def __str__(self):
        return self.user.get_full_name() + ' '+  self.title


