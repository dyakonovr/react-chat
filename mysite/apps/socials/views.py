from urllib import parse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
import configparser


# Create your views here.
@login_required
def vk_auth(request):
    params = {
        'client_id': '	51571624',
        'redirect_uri': 'http://127.0.0.1:8000',
        'response_type': 'token',
        'scope': 'friends',
        'display': 'popup'
    }
    return redirect('https://oauth.vk.com/authorize?' + parse.urlencode(params))
    return redirect('profile')


@login_required
def vk_link(request):
    code = request.GET.get('code')
    params = {
        'client_id': '51571624',
        # 'client_secret': 'mBeaBdPB9PURo9LsuH5h',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'code': code,
    }
    req = requests.get('https://oauth.vk.com/access_token?', params=params)

    data = req.json()
    access_token = data['access_token']
    print(data)
    current_user = request.user.username
    config = configparser.ConfigParser()
    path = f'../users/kirinw8/config.ini'
    config.read(path)
    print(access_token)
    # config.set("VK", "access_token", access_token)
    # with open(path, 'w')as file:
    #     config.write(file)
    return redirect("profile")


@login_required
def wa_link(request):
    pass
