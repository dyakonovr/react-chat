from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


def getUserData(request):
    username = request.user.username
    email = request.user.email
    data = {
        'username': username,
        'email': email,
    }
    return JsonResponse(data)
