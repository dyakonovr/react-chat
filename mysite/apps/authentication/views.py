from django.shortcuts import render, redirect
from .forms import LogInForm, SignUpForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


import os
import shutil


def login(request):
    if not request.user.is_authenticated:
        logInForm = LogInForm()
        if request.method == 'POST':
            form = LogInForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(
                    username=cd['username'], password=cd['password'])
                if user is not None:
                    auth_login(request, user)
                    return redirect("main")
                else:
                    messages.error(request, "Invalid login or password")
                    return redirect('login')
            else:
                form = LogInForm()
        return render(request, 'logIn.html', {"form": logInForm})
    else:
        return redirect('main')


def signUp(request):
    if not request.user.is_authenticated:
        def createFolder(username):
            folderPath = 'users' 
            if not os. path.exists(folderPath):
                os.mkdir('users')
            toFolder = "users/" + username
            fromFolder = "scripts/"
            os.mkdir(toFolder)
            os.mkdir("users/" + username + "/jsons")
            if (os.path.exists(fromFolder) and os.path.exists(toFolder)):
                for file in os.listdir(fromFolder):
                    if os.path.isfile(os.path.join(fromFolder, file)):
                        shutil.copy(os.path.join(fromFolder, file),
                                    os.path.join(toFolder, file))
                    if os.path.isdir(os.path.join(fromFolder, file)):
                        os.system(f'rd /S /Q {toFolder}/{file}')
                        shutil.copytree(os.path.join(fromFolder, file),
                                        os.path.join(toFolder, file))
            with open(toFolder + '/config.ini', 'w') as file:
                file.write('[Telegram]\n')
                file.write('api_id = \n')
                file.write('api_hash = \n')
                file.write('[VK]\n')
                file.write('access_token = \n')
                file.write('[INST]\n')
                file.write('number = \n')
                file.write('password = \n')
                file.write('[WA]\n')
                file.write('id = \n')
                file.write('token = ')

        if (request.method == 'POST'):
            form = SignUpForm(request.POST)
            if (form.is_valid()):
                user = form.save(commit=False)
                user.set_password(user.password)
                user.save()
                auth_login(request, user)
                createFolder(user.username)
                return redirect("main")
        else:
            form = SignUpForm()
        return render(request, 'signUp.html', {"form": form})
    else:
        return redirect('main')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
