# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import *
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect


def register(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        return render(request, 'user_form/home.html', {'user': user})
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email']
                )
                return render(request, 'user_form/home.html', {'user': user})
        else:
            form = UserForm()
        return render(request, 'user_form/register.html', {'form': form})


def register_success(request):
    if request.user.is_authenticated:
        return render(request, 'user_form/success.html')
    else:
        return render(request, 'user_form/register.html')


def logout_page(request):
    logout(request)
    return render(request, 'user_form/index.html')


def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'user_form/home.html', )
            else:
                return render(request, 'user_form/index.html', {'error_message': "account has been disable"})
        else:
            return render(request, 'user_form/index.html', {"error_message": "Invalid login"})
    return render(request, 'user_form/index.html', {"error_message": "Login to Enter"})


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        return render(request, 'user_form/home.html', {"user": user})
    else:
        return render(request, 'user_form/index.html', )


def change_pass(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('user_form/index.html')
    else:
        return render(request, 'user_form/resetPassword.html', )


def reset(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('user_form/index.html')
    else:
        if request.method == "POST":
            pass1 = request.POST['password1']
            pass2 = request.POST['password2']
            if pass1 != pass2:
                return render(request, 'user_form/home.html',
                              {'error_message': 'mismatch password and password again !'})
            else:
                user = User.objects.get(username=request.user)
                user.set_password(pass1)
                user.save()
                return render(request, 'user_form/home.html', {'error_message': 'password changed successfully '})
