from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import User


def user_register(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required(login_url='users:login')
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'users/profile.html', {'form': form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        return redirect('users:profile')
    return render(request, 'users/profile_view.html', {
        'user_profile': user,
    })


@login_required(login_url='users:login')
def user_logout(request):
    logout(request)
    return redirect('users:login')
