from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile, LoginLog
import json

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from weather.services import get_current_weather

"""

@csrf_exempt
def register_api(request):

    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if not all([username, email, phone, password, confirm_password]):
            return JsonResponse({'status': 'error', 'message': 'All fields are required'})

        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', 'message': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        # Create the Profile linked to this User:
        Profile.objects.create(user=user, phone=phone)

        return JsonResponse({'status': 'success', 'message': 'User registered successfully'})

    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'})



@csrf_exempt
def login_api(request):

    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    
    if request.method == 'POST':
        data = json.loads(request.body)

        username_or_email = data.get('username')
        password = data.get('password')

        if not username_or_email or not password:
            return JsonResponse({'status': 'error', 'message': 'Username/email and password are required'})

        user = authenticate(username=username_or_email, password=password)
        if not user:
            # Try with email if username failed
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            login(request, user)
            # Create a login log entry
            LoginLog.objects.create(user=user)
            return JsonResponse({'status': 'success', 'message': 'Login successful'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})

    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'})


"""

def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if password != confirm:
            return render(request, 'register.html', {'message': 'Passwords do not match'})

        if User.objects.filter(username=name).exists():
            return render(request, 'register.html', {'message': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'message': 'Email already exists'})

        user = User.objects.create_user(username=name, email=email, password=password)
        Profile.objects.create(user=user, phone=phone)

        return redirect('/login/')
    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            # Try logging in using email
            try:
                user_obj = User.objects.get(email=username)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            login(request, user)
            LoginLog.objects.create(user=user)
            return redirect('/home/')
        else:
            return render(request, 'login.html', {'message': 'Invalid credentials'})
    return render(request, 'login.html')


@login_required(login_url='/login/')
def home_page(request):
    city = request.GET.get('city')
    weather = None
    error = None
    if city:
        data = get_current_weather(city)
        if 'error' in data:
            error = data['error']
        else:
            weather = data
    return render(request, 'home.html', {'weather': weather, 'error': error})


def logout_page(request):
    django_logout(request)
    return redirect('login')
