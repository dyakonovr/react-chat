from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    current_user = request.user
    username = current_user.username
    email = current_user.email
    phoneNumber = current_user.phoneNumber
    code = ''
    if request.GET.get('code'):
        code = request.GET.get('code')
    content = {
        'username': username,
        'email': email,
        'phoneNumber': phoneNumber,
        'code' : code,
    }
    return render(request, 'profile.html', context=content)

