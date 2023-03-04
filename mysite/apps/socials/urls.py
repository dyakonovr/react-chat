from django.urls import path
from . import views

urlpatterns = [
    path('vk_auth', views.vk_auth, name='vk-auth'),
    path('vk_link', views.vk_link, name="vk-link")
]
