from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

from base.models import User


class Profile(models.Model):
    """Model for profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headline = models.TextField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/', default='avatar.png')
    bio = models.TextField(max_length=500, null=True, blank=True)
    gender = models.CharField(choices=[('m','Male'),('f','Female')], max_length=1)
    age = models.IntegerField(validators=[MinValueValidator(18),])

    def __str__(self):
        return str(self.user)


