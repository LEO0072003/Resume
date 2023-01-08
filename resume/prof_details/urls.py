from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/<str:username>/', login_required(views.ProfileView.as_view(),login_url='login'), name='profile'),

    path('milestone/<str:id>/', login_required(views.MilestoneView.as_view(),login_url='login'), name='milestone'),
    path('profile_edit/', login_required(views.ProfileEditDetails.as_view(),login_url='login'), name='edit_profile'),
    path('detail_list/', login_required(views.ProfileEditDetails.as_view(),login_url='login'), name='detail'),
    path('profile_edit/<str:pk>/', login_required(views.ProfileEditDetails.as_view(),login_url='login'), name='edit_spc_profile'),
    path('add_details/', login_required(views.ProfileEditDetails.as_view(),login_url='login'), name='add_details'),
    path('delete/<str:pk>/', login_required(views.deleteProfileDetail,login_url='login'), name='delete'),
    path('view_resume/', views.view_profile, name='view_profile')

]
