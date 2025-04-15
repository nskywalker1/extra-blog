from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import login, authenticate, logout


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
