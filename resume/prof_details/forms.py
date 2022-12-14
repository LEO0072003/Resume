from django import forms
from .models import Profile, WorkExperiences, Academics, Certifications, Skill, Contact
from base.models import Milestones
from django.forms import HiddenInput


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        # exclude = ['avatar']
        fields = '__all__'
        widgets  =  {'user': HiddenInput()}


class WorkexperienceEditForm(forms.ModelForm):
    class Meta:
        model = WorkExperiences
        fields = '__all__'
        widgets  =  {'user': HiddenInput()}



class AcademicsEditForm(forms.ModelForm):
    class Meta:
        model = Academics
        fields = '__all__'
        widgets  =  {'profile': HiddenInput()}


class CertificationsEditForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = '__all__'
        widgets  =  {'user': HiddenInput()}


class MilestonesEditForm(forms.ModelForm):
    class Meta:
        model = Milestones
        fields = '__all__'
        widgets  =  {'user': HiddenInput()}


class SkillEditForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets  =  {'user': HiddenInput()}


class ContactEditForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets  =  {'user': HiddenInput()}
