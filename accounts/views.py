import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout


from django.contrib import messages

# Create your views here.
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()

    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)

        if(form.is_valid()):
            form.save()
            messages.success(request, f'Account created for {form.cleaned_data["username"]}!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {username}')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
