from django.contrib.auth.decorators import login_required
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
        if User.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'Bu foydalanuvchi allaqachon mavjud')
            return redirect('register_page')
        user = User.objects.create_user(username=username, phone_number=phone_number, email=email, password=password)

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('index_page')
    return render(request, 'accounts/register.html')


def login_page(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = authenticate(request, username=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('index_page')
        else:
            messages.error(request, "Telefon raqam yoki parol noto‘g‘ri!")
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required
def index_page(request):
    return render(request, 'accounts/index.html')
