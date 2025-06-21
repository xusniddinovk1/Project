from django.shortcuts import render, redirect
from core.models import AboutUs, News, Course, Lesson
from dashboard.forms import AboutUsForm, NewsForm, CourseForm, LessonForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")
        remember = request.POST.get("remember_me")  # checkbox nomi

        user = authenticate(request, phone_number=phone, password=password)
        if user:
            login(request, user)

            if not remember:
                # Sessiyani brauzer yopilganda tugatish
                request.session.set_expiry(0)

            return redirect("home_page")
        else:
            return render(request, "dashboard/login.html", {"error": "Incorrect credentials"})

    return render(request, "dashboard/login.html")


def signup_page(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 🔐 1. Bo‘sh maydonlar
        if not phone_number or not password or not confirm_password:
            return render(request, 'dashboard/signup.html', {
                'error': 'All fields are required.'
            })

        # 🔐 2. Parollar mos emas
        if password != confirm_password:
            return render(request, 'dashboard/signup.html', {
                'error': 'Passwords do not match.'
            })

        # 🔐 3. Minimal parol uzunligi
        if len(password) < 6:
            return render(request, 'dashboard/signup.html', {
                'error': 'Password must be at least 6 characters long.'
            })

        # 🔐 4. Raqam allaqachon ro‘yxatdan o‘tgan
        if User.objects.filter(phone_number=phone_number).exists():
            return render(request, 'dashboard/signup.html', {
                'error': 'Phone number is already registered.'
            })

        # ✅ 5. Foydalanuvchini yaratish
        user = User.objects.create_user(phone_number=phone_number, password=password)

        # 🔓 6. Login qilish
        user = authenticate(request, phone_number=phone_number, password=password)
        if user:
            login(request, user)
            return redirect('home_page')  # Sahifani moslashtiring

    return render(request, 'dashboard/signup.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required_decorator
def home_page(request):
    news = News.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()

    ctx = {
        "count": {
            'news': len(news),
            'courses': len(courses),
            'lessons': len(lessons),
        }
    }
    return render(request, 'dashboard/index.html', ctx)
