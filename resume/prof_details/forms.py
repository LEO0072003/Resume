from django import forms
from .models import Profile, WorkExperiences, Academics, Certifications
from base.models import Milestones
from django.forms import HiddenInput


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets  =  {'user': HiddenInput()}


class WorkexperienceEditForm(forms.ModelForm):
    class Meta:
        model = WorkExperiences
        fields = '__all__'


class AcademicsEditForm(forms.ModelForm):
    class Meta:
        model = Academics
        fields = '__all__'


class CertificationsEditForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = '__all__'


class MilestonesEditForm(forms.ModelForm):
    class Meta:
        model = Milestones
        fields = '__all__'
