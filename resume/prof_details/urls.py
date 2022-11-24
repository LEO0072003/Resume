from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/<str:username>', login_required(views.ProfileView.as_view(),login_url='login'), name='profile'),

]
