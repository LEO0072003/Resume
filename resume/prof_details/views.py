from django.shortcuts import render, redirect
from django.views import View
from .models import Profile
# Create your views here.



class ProfileView(View):

    def get(self, request, *args, **kwargs):
        username = request.user.username
        profile = Profile.objects.get(user=request.user)
        print(profile)
        context = {'profile': profile}
        return render(request,'prof_details/profile.html', context)
