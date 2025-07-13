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



from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def dashboard_redirect(request):
    user = request.user
    if user.role == 'doctor':
        return redirect('doctor_dashboard')
    elif user.role == 'radiologist':
        return redirect('radiologist_dashboard')
    elif user.role == 'patient':
        return redirect('patient_dashboard')
    elif user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('/')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/dashboard_doctor.html')

@login_required
def radiologist_dashboard(request):
    return render(request, 'accounts/dashboard_radiologist.html')

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/dashboard_patient.html')
