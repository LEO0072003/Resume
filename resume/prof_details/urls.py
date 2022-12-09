from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/<str:username>/', login_required(views.ProfileView.as_view(),login_url='login'), name='profile'),
    path('milestone/<str:id>/', login_required(views.MilestoneView.as_view(),login_url='login'), name='milestone'),
    path('profile_edit/', views.ProfileEditDetails.as_view(), name='edit_profile'),
    path('detail_list/', views.ProfileEditDetails.as_view(), name='detail'),
    path('profile_edit/<str:pk>/', views.ProfileEditDetails.as_view(), name='edit_spc_profile'),
]
