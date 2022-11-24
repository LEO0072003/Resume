from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm

# Create your views here.


class Home(View):

    def get(self,request,*args,**kwargs):
        return render(request,'base/home.html')

def loginPage(request):

    page = 'login'

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Not a valid user')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'base/login_register.html', {'page':page})

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = MyUserCreationForm()
    page = 'register'

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            return redirect('home')

        else:
            messages.error(request, 'Invalid Details')

    context = {'page':page, 'form':form}
    return render(request, 'base/login_register.html', context)



