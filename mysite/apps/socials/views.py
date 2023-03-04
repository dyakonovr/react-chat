from urllib import parse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import VkLink
from .models import SocialsLinks


@login_required
def vk_auth(request):
    params = {
        'client_id': '6287487',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'response_type': 'token',
        'scope': 501202911,
        'display': 'page'
    }
    return redirect('https://oauth.vk.com/authorize?' + parse.urlencode(params))


@login_required
def wa_link(request):
    pass


@login_required
def profile(request):

    current_user = request.user
    username = current_user.username
    email = current_user.email
    phoneNumber = current_user.phoneNumber
    user_id = current_user.id

    flag = True
    flagLink = True

    if request.method == 'POST':
        form = VkLink(request.POST)
        if form.is_valid():
            object = form.save(commit=False)

            object.user_id = user_id

            url = object.vk_token
            token = url.split('access_token=')
            object.vk_token = token[1]

            object.save()

            return redirect('profile')
    else:
        form = VkLink()

    if SocialsLinks.objects.filter(user_id=user_id).exists():
        flagLink = False
        flag = False

    content = {
        'username': username,
        'email': email,
        'phoneNumber': phoneNumber,
        'flag': flag,
        'flagLink': flagLink,
        'form': form,
    }

    return render(request, 'profile.html', context=content)
