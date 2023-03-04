from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^profile', views.profile, name='profile'),
    path('vk_auth', views.vk_auth, name='vk-auth'),
]
