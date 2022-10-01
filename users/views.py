from multiprocessing import context
from re import I
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from . forms import *
# Create your views here.
def loginForm(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'you are sucessfully login')
            return redirect('/')
            
        else:
            messages.info(request, 'Username or password wrong')
    context = {}
    return render(request, 'users/login.html', context)

def logoutForm(request):
    logout(request)
    messages.info(request, 'You are successfully Logout')
    return redirect('login')


def registerForm(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.info(request, 'Account was created')
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username Or password not match')
    context = {'form': form}
    return render(request, 'users/registration.html', context)
