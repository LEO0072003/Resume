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
            # print(academics)
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

# def createProfilePage(request):
#     """Page for editing user"""
#     if request.method == 'GET':
#         page = 'edit'
#         r = request.GET.get('r')
#         profile = Profile.objects.get(user=request.user)
#         context={'page':page, 'profile': profile}

#         if (r == 'profile'):
#             # Fetching Profile object
#             try:
#                 form = ProfileEditForm(initial={
#                                                 'user':request.user,
#                                                 'headline': profile.headline,
#                                                 'avatar': profile.avatar,
#                                                 'bio': profile.bio,
#                                                 'gender': profile.gender,
#                                                 'age': profile.age
#                                                 })
#                 form.fields['user'].widgets = HiddenInput()
#                 context.update({'form':form})
#             except:
#                 pass

#         elif (r == 'academics'):
#             # Fetching Academics object
#             try:
#                 academics = Academics.objects.filter(profile=profile).values()
#                 print(academics)
#                 form = AcademicsEditForm(initial={
#                                                 'profile':profile,
#                                                 'degree': academics[0].get('degree'),
#                                                 'year_of_completion':academics[0].get('year_of_completion')
#                                                                                             })
#                 form.fields['profile'].widgets = HiddenInput()
#                 context.update({'obj':academics, 'form':form})
#             except:
#                 pass

#         # elif (r == 'projects'):
#         #     # Fetching Milestone object
#         #     try:
#         #         form = MilestonesEditForm()
#         #         milestones = Milestones.objects.filter(user=request.user)
#         #         context.update({'obj':milestones, 'form':form})
#         #     except:
#         #         pass

#         # elif (r == 'certification'):
#         #     # Fetching Certification object
#         #     try:
#         #         form = CertificationsEditForm()
#         #         certif = Certifications.objects.filter(user=request.user).values()
#         #         context.update({'obj':certif, 'form':form})
#         #     except:
#         #         pass

#         # elif (r == 'experience'):
#         #     # Fetching WorkExperience object
#         #     try:
#         #         form = WorkexperienceEditForm(initial={
#         #                                         'user':request.user,
#         #                                         'degree':
#         #                                         })
#         #         workex = WorkExperiences.objects.filter(user=request.user)
#         #         context.update({'obj':workex, 'form':form})

#         #     except:
#         #         pass

#         # print(context)
#         print(request.method)
#         # print(request.POST)

#         return render(request, 'prof_details/profile.html',context)
#     elif request.method =='POST':
#         print(request.POST,'\n')
#         print(form)
#         context={}
#         return render(request, 'prof_details/profile.html',context)


class ProfileEditDetails(View):
    """Views for editing profile"""
    page = 'edit'
    context = {'page': page}

    def select_form(self, req_post=None, req_files=None, id=None):
        # print(data)
        r = self.request.GET.get('r')
        profile = Profile.objects.get(user = self.request.user)
        self.context.update({'profile':profile, 'r':r})

        # Profile Form
        if r == 'profile':
            form = ProfileEditForm(req_post, req_files, instance = profile)
            return form

        # Certification Form
        elif r == 'certification':
            if id==None:
                certifications = Certifications.objects.filter(user=self.request.user)

                return certifications
            else:
                certifications = Certifications.objects.get(id=id)
                form = CertificationsEditForm(req_post, req_files ,instance=certifications)
                return form

        # Academics Form
        elif r == 'academics':
            if id == None:
                academics = Academics.objects.filter(profile=profile)
                return academics
            else:
                academics = Academics.objects.get(id=id)
                form = AcademicsEditForm(req_post, req_files ,instance=academics)
                return form

        #Work Experience Form
        elif r == 'experience':
            if id == None:
                experience = WorkExperiences.objects.filter(user = self.request.user)
                return experience
            else:
                experience = WorkExperiences.objects.get(id=id)
                form = WorkexperienceEditForm(req_post, req_files ,instance=experience)
                return form

        #Projects Form
        elif r == 'projects':
            if id == None:
                projects = Milestones.objects.filter(user = self.request.user)
                return projects
            elif id:
                projects = Milestones.objects.get(id=id)
                form = MilestonesEditForm(req_post, req_files ,instance=projects)
                return form



    def get(self, request, *args, **kwargs):

        if not self.request.GET.get('d'):
            """Edit pages rendered after detail_list pages"""

            if kwargs.get('pk'):
                print("reached")
                form = self.select_form(id= kwargs.get('pk'))

            else:
                """Form rendered only for profile page"""
                form = self.select_form()

            self.context.update({'form':form})

            return render(request, 'prof_details/profile.html', self.context)

        elif self.request.GET.get('d'):
            """Detailed list page """

            obj = self.select_form()
            self.context.update({'obj':obj})
            return render(request, 'prof_details/details_list.html', self.context)

    def post(self, request, *args, **kwargs):
        form = self.select_form(request.POST, request.FILES, kwargs.get('pk'))
        # print("form-data:",form.data)
        if form.is_valid():
            form.save(commit=False)

            print(form.cleaned_data)
            # if 'avatar' in form.cleaned_data:
            #     print(form.cleaned_data)
                # if form.cleaned_data.get('avatar') is False:
                #     form.cleaned_data['avatar'] =
                    # pass
            form.save()

            return redirect('home')
        else:
            print('error: ',form.errors)

        return render(request, 'prof_details/profile.html')
