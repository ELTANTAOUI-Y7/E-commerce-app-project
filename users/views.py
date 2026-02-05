from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def profile(request):
    """User profile placeholder view."""
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'user': request.user,
    }
    return render(request, 'users/profile.html', context)


def login_view(request):
    """User login view."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
    
    return render(request, 'users/login.html')


def register_view(request):
    """User registration view."""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password == password_confirm:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('home')
            except:
                context = {'error': 'Username already exists'}
                return render(request, 'users/register.html', context)
        else:
            context = {'error': 'Passwords do not match'}
            return render(request, 'users/register.html', context)
    
    return render(request, 'users/register.html')


def logout_view(request):
    """User logout view."""
    logout(request)
    return redirect('home')
