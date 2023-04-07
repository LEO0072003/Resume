from django.forms import HiddenInput
from resume.settings import MEDIA_ROOT
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

from .models import (
                    Profile,
                    Academics,
                    Certifications,
                    WorkExperiences,
                    Skill,
                    Contact
                    )

from .forms import (
                    AcademicsEditForm,
                    WorkexperienceEditForm,
                    ProfileEditForm,
                    CertificationsEditForm,
                    MilestonesEditForm,
                    SkillEditForm,
                    ContactEditForm

                    )
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
            # print(request.user)
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

    def select_form(self, req_post=None, req_files=None, id=None, f=False):
        r = self.request.GET.get('r')
        profile = Profile.objects.get(user = self.request.user)
        self.context.update({'profile':profile, 'r':r})

        # Profile Form
        if r == 'profile':
            form = ProfileEditForm(req_post, req_files, instance = profile)
            return form

        # Certification Form
        elif r == 'certification':
            form = CertificationsEditForm(req_post, req_files, initial={'user':self.request.user})
            if id==None and not f:
                certifications = Certifications.objects.filter(user=self.request.user)

                return certifications
            elif id:
                certifications = Certifications.objects.get(id=id)
                form = CertificationsEditForm(req_post, req_files ,instance=certifications)
                return form

            return form

        # Academics Form
        elif r == 'academics':
            form = AcademicsEditForm(req_post, req_files, initial={'profile':profile})
            if id == None and not f:
                academics = Academics.objects.filter(profile=profile)
                return academics
            elif id:
                academics = Academics.objects.get(id=id)
                form = AcademicsEditForm(req_post, req_files ,instance=academics)
                return form

            return form

        #Work Experience Form
        elif r == 'experience':
            form = WorkexperienceEditForm(req_post, req_files,initial={'user':self.request.user})
            if id == None and not f:
                experience = WorkExperiences.objects.filter(user = self.request.user)
                return experience
            elif id:
                experience = WorkExperiences.objects.get(id=id)
                form = WorkexperienceEditForm(req_post, req_files ,instance=experience)
                return form

            return form

        #Projects Form
        elif r == 'projects':
            form = MilestonesEditForm(req_post, req_files,initial={'user':self.request.user})
            if id == None and not f:
                projects = Milestones.objects.filter(user = self.request.user)
                return projects
            elif id:
                projects = Milestones.objects.get(id=id)
                form = MilestonesEditForm(req_post, req_files ,instance=projects)
                return form
            return form

        #Skills Form
        elif r == 'skills':
            form = SkillEditForm(req_post, req_files,initial={'user':self.request.user})
            if id == None and not f:
                skill = Skill.objects.filter(user = self.request.user)
                return skill
            elif id:
                skill = Skill.objects.get(id=id)
                form = SkillEditForm(req_post, req_files ,instance=skill)
                return form
            return form

        #Contacts Form
        elif r == 'contacts':
            form = ContactEditForm(req_post, req_files,initial={'user':self.request.user})
            if id == None and not f:
                contacts = Contact.objects.filter(user = self.request.user)
                return contacts
            elif id:
                contacts = Contact.objects.get(id=id)
                form = ContactEditForm(req_post, req_files , instance=contacts)
                return form
            return form


    def get(self, request, *args, **kwargs):
        self.context.update({'r':self.request.GET.get('r')})
        if not self.request.GET.get('d') and not self.request.GET.get('a'):
            """Edit pages rendered after detail_list pages"""

            if kwargs.get('pk'):
                form = self.select_form(id= kwargs.get('pk'))

            else:
                """Form rendered only for profile page"""
                form = self.select_form()
            # print("form-data: ",form.instance.id)
            self.context.update({'form':form})

            return render(request, 'prof_details/profile.html', self.context)

        elif self.request.GET.get('d'):
            """Detailed list page """

            obj = self.select_form()
            self.context.update({'obj':obj})
            return render(request, 'prof_details/details_list.html', self.context)

        elif self.request.GET.get('a'):
            """Form rendered after user requests for add"""
            form = self.select_form(f=True)
            print('form')

            self.context.update({'form':form})
            return render(request, 'prof_details/profile.html', self.context)

    def post(self, request, *args, **kwargs):
        vals = kwargs.get('pk')
        a = self.request.GET.get('a')
        r = self.request.GET.get('r')
        f = False
        if a :
            f = True
        # print(f)
        form = self.select_form(request.POST, request.FILES, vals, f)

        if form.is_valid():
            form.save(commit=False)


            if 'avatar' in form.cleaned_data:
                # print(form.cleaned_data)
                if form.cleaned_data.get('avatar') is False:
                    form.cleaned_data['avatar'] = MEDIA_ROOT / 'avatar.png'

            form.save()

            if r=='profile':
                return redirect(f'/detail_list/?r={r}')

            else:
                return redirect(f'/detail_list/?r={r}&d=details')

        else:
            print('error: ',form.errors)

        return render(request, 'prof_details/profile.html')


def deleteProfileDetail(request, pk):
    r = request.GET.get('r')

    if r == 'experience':
        obj = WorkExperiences.objects.get(id=pk)
    elif r == 'certification':
        obj = Certifications.objects.get(id=pk)
    elif r == 'academics':
        obj = Academics.objects.get(id=pk)
    elif r == 'projects':
        obj = Milestones.objects.get(id=pk)

    obj.delete()
    return redirect('edit_profile')

def view_profile(request, pk):
    """Method for showing your resume to other people"""
    context = {'user_id':int(pk)}
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
        milestones = Milestones.objects.filter(user=pk)
        context.update({'milestones':milestones})
    except:
        pass

    # Fetching Certification objects
    try:
        certif = Certifications.objects.filter(user=pk).values()
        context.update({'certifications':certif})
    except:
        pass

    # Fetching WorkExperience objects
    try:
        workex = WorkExperiences.objects.filter(user=pk).values()
        context.update({'workexperience':workex})
    except:
        pass

    # Fetching Skill objects
    try:
        skill = Skill.objects.filter(user=pk).values()
        context.update({'skill':skill})
    except:
        pass

    try:
            contacts = Contact.objects.filter(user=pk)[0]
            context.update({'contacts':contacts})

    except:
        pass
    # print(type(context.get('user_id')))
    return render(request,'prof_details/view_profile.html', context)

