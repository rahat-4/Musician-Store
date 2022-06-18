from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from login_app.forms import UserRegister, UserRegisterMore
from login_app.models import User, UserInfo


# Create your views here.


def user_registration(request):
    registered = False
    user_info = UserRegister()
    user_info_more = UserRegisterMore()

    if request.method == 'POST':
        user_info = UserRegister(data=request.POST)
        user_info_more = UserRegisterMore(data=request.POST)

        if user_info.is_valid() and user_info_more.is_valid():
            user_i = user_info.save(commit=False)
            user_i.set_password(user_i.password)
            user_i.save()

            user_info_i = user_info_more.save(commit=False)
            user_info_i.user = user_i

            if 'profile_pic' in request.FILES:
                user_info_i.profile_pic = request.FILES['profile_pic']

            user_info_i.save()
            registered = True

    dict = {'user_info': user_info,
            'user_info_more': user_info_more, 'registered': registered}
    return render(request, 'login_app/user_registration.html', dict)


def user_login(request):
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)

    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')

    #         user = authenticate(request, username=username, password=password)
    #         print(user)

    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 HttpResponseRedirect(reverse('musician_info:index'))
    #             else:
    #                 HttpResponse("Account deleted!")
    #         else:
    #             HttpResponse("Wrong information!")
    # else:
    #     form = LoginForm()
    dict = {}
    return render(request, 'login_app/user_login.html', dict)


def login_func(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('login_app:user_profile', kwargs={'user_id': user.id}))
            else:
                HttpResponse("Account deleted!")
        else:
            HttpResponse("Wrong information!!")
    else:
        return HttpResponseRedirect(reverse('login_app:user_login'))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('musician_info:index'))


@login_required
def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user_info = UserInfo.objects.get(user__pk=user_id)
    dict = {'user': user, 'user_info': user_info}
    return render(request, 'login_app/user_profile.html', dict)
