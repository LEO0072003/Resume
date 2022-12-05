from django.forms import HiddenInput
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Profile, Academics, Certifications, WorkExperiences
from .forms import AcademicsEditForm, WorkexperienceEditForm, ProfileEditForm, CertificationsEditForm, MilestonesEditForm
from base.models import Milestones
# Create your views here.



class ProfileView(View):

    def get(self, request, *args, **kwargs):
        username = request.user.username
        page = 'ViewProfile'
        context = {'page':page}

        # Fetching Profile object
        try:
            profile = Profile.objects.get(user=request.user)
            context.update({'profile': profile})
        except:
            messages.error(request,'Havent set up a profile yet')

        # Fetching Academics object
        try:
            academics = Academics.objects.filter(profile=profile)
            context.update({'academics':academics})
        except:
            pass

        # Fetching Milestone object
        try:
            milestones = Milestones.objects.filter(user=request.user)
            context.update({'milestones':milestones})
        except:
            pass

        # Fetching Certification object
        try:
            certif = Certifications.objects.filter(user=request.user).values()
            context.update({'certifications':certif})
        except:
            pass

        # Fetching WorkExperience object
        try:
            workex = WorkExperiences.objects.filter(user=request.user)
            context.update({'workexperience':workex})
        except:
            pass



        return render(request,'prof_details/profile.html', context)


class MilestoneView(View):

    def get(self, request, *args, **kwargs):
        milestones = Milestones.objects.get(id=kwargs.get('id'))
        context = {'milestones':milestones}

        return render(request, 'base/milestones_page.html',context)

def createProfilePage(request):
    """Page for editing user"""
    if request.method == 'GET':
        page = 'edit'
        r = request.GET.get('r')
        profile = Profile.objects.get(user=request.user)
        context={'page':page, 'profile': profile}

        if (r == 'profile'):
            # Fetching Profile object
            try:
                form = ProfileEditForm(initial={
                                                'user':request.user,
                                                'headline': profile.headline,
                                                'avatar': profile.avatar,
                                                'bio': profile.bio,
                                                'gender': profile.gender,
                                                'age': profile.age
                                                })
                form.fields['user'].widgets = HiddenInput()
                context.update({'form':form})
            except:
                pass

        elif (r == 'academics'):
            # Fetching Academics object
            try:
                academics = Academics.objects.filter(profile=profile).values()
                print(academics[0].get('degree'))
                form = AcademicsEditForm(initial={
                                                'profile':profile,
                                                'degree': academics[0].get('degree'),
                                                'year_of_completion':academics[0].get('year_of_completion')
                                                                                            })
                form.fields['profile'].widgets = HiddenInput()
                context.update({'obj':academics, 'form':form})
            except:
                pass

        # elif (r == 'projects'):
        #     # Fetching Milestone object
        #     try:
        #         form = MilestonesEditForm()
        #         milestones = Milestones.objects.filter(user=request.user)
        #         context.update({'obj':milestones, 'form':form})
        #     except:
        #         pass

        # elif (r == 'certification'):
        #     # Fetching Certification object
        #     try:
        #         form = CertificationsEditForm()
        #         certif = Certifications.objects.filter(user=request.user).values()
        #         context.update({'obj':certif, 'form':form})
        #     except:
        #         pass

        # elif (r == 'experience'):
        #     # Fetching WorkExperience object
        #     try:
        #         form = WorkexperienceEditForm(initial={
        #                                         'user':request.user,
        #                                         'degree':
        #                                         })
        #         workex = WorkExperiences.objects.filter(user=request.user)
        #         context.update({'obj':workex, 'form':form})

        #     except:
        #         pass

        # print(context)
        print(request.method)
        # print(request.POST)

        return render(request, 'prof_details/profile.html',context)
    elif request.method =='POST':
        print(request.POST,'\n')
        print(form)
        context={}
        return render(request, 'prof_details/profile.html',context)

class ProfileEditDetails(View):
    """Views for editing profile"""
    page = 'edit'
    context = {'page': page}

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileEditDetails, self).get_context_data(**kwargs)
    #     context['page'] = self.page
    #     # context['r'] = self.request.GET.get('r')
    #     print(context)
    #     return context

    def select_form(self, data=None):
        # print(data)
        r = self.request.GET.get('r')
        profile = Profile.objects.get(user = self.request.user)
        self.context.update({'profile':profile})

        # Profile Form
        if r == 'profile':
            form = ProfileEditForm(data, instance= profile)
            # print(form.data)
            return form

        # Certification Form
        elif r == 'certification':
            certifications = Certifications.objects.filter(user=self.request.user).values()[0]
            form = CertificationsEditForm(instance=certifications)
            return form

        # Academics Form
        # elif r == 'academics':
        #     academics = Academics.objects.filter(profile=profile).values()
        #     form = AcademicsEditForm(initial={
        #                                         'profile':profile,

        #     })



    def get(self, request, *args, **kwargs):
        form = self.select_form()
        self.context.update({'form':form})
        # print(self.context)
        return render(request, 'prof_details/profile.html', self.context)

    def post(self, request, *args, **kwargs):

        form = self.select_form(request.POST)
        # print("form-data:",form.data)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect('home')
        else:
            print('error: ',form.errors)

        return render(request, 'prof_details/profile.html')
