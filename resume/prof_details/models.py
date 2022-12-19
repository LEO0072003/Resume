from django.db import models
from django.core.validators import MinValueValidator
import datetime
# Create your models here.

from base.models import User


class Profile(models.Model):
    """Model for profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headline = models.TextField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/', default='avatar.png')
    bio = models.TextField(max_length=500, null=True, blank=True)
    gender = models.CharField(choices=[('m','Male'),('f','Female')], max_length=1, null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(18),], null=True, blank=True)

    # def __str__(self):
    #     return str(self.user)


class Academics(models.Model):
    """Model for academic achievements"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, null=True, blank=True)
    year_of_completion = models.IntegerField(choices=[(r,r) for r in range(1950,datetime.date.today().year+10)],
                                             default=datetime.date.today().year, null=True, blank=True)

    # def __str__(self):
    #     if self.degree:
    #         return self.degree
    #     else :
    #         return self.profile.user


class Certifications(models.Model):
    """Model for certifications"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=20, null=True, blank=True)
    certifications = models.FileField(upload_to='certifications/' ,null=True, blank=True)

    # def __str__(self):
    #     if self.title:
    #         return self.title
    #     else :
    #         return self.user


class WorkExperiences(models.Model):
    """Model for work experiences"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=30, null=True, blank=True)
    year_joined = models.IntegerField(choices=[(r,r) for r in range(1950,datetime.date.today().year)],
                                             default=datetime.date.today().year-10, null=True, blank=True)
    year_left = models.IntegerField(choices=[(r,r) for r in range(1950,datetime.date.today().year)],
                                             default=datetime.date.today().year-1, null=True, blank=True)

    # def __str__(self):
    #     if self.organization_name and self.designation:
    #         return self.organization_name + ' ' +  self.designation
    #     else:
    #         return self.user
