from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .forms import RegisterForm

# Helper to get the user's role
def get_user_role(user):
    if user.groups.filter(name='doctor').exists():
        return 'doctor'
    elif user.groups.filter(name='radiologist').exists():
        return 'radiologist'
    elif user.is_superuser:
        return 'admin'
    return 'user'

# Register view with role assignment
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            group, created = Group.objects.get_or_create(name=role)
            user.groups.add(group)
            login(request, user)

            # Redirect after registration
            if role == 'doctor':
                return redirect('upload')
            elif role == 'radiologist':
                return redirect('home')
            elif role == 'admin':
                return redirect('/admin/')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login view with role-based redirect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            role = get_user_role(user)
            if role == 'doctor':
                return redirect('upload')
            elif role == 'radiologist':
                return redirect('home')  # or 'reports'
            elif role == 'admin':
                return redirect('/admin/')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'accounts/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
