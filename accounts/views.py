from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(phone_number=phone_number).exicts():
            messages.error(request, 'Bu foydalanuvchi allaqachon mavjud')
            return redirect('register_page')
        user = User.objects.create_user(username=username, phone_number=phone_number, email=email, password=password)
        login(request, user)
        return redirect('course_detail')
    return render(request, 'accounts/register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('course_detail')
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri!")
            return redirect('login_page')
    return render(request, 'accounts/login.html')


def logout_page(request):
    logout(request)
    return redirect('login_page')
