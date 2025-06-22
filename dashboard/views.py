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


# ================= News =================
def about_us_list(request):
    AboutUs.objects.alL()
    ctx = {
        'text': text
    }
    return render(request, 'dashboard/about_us/list.html', ctx)


def about_us_create(request):
    model = AboutUs()
    form = AboutUsForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('about_us_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/about_us/form.html', ctx)


def about_us_edit(request, pk):
    model = AboutUs.objects.get(pk=pk)
    form = AboutUsForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('about_us_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/about_us/form.html', ctx)


def about_us_delete(request, pk):
    model = AboutUs.objects.get(pk=pk)
    model.delete()
    return redirect('about_us_list')


# ================= News =================
def news_list(request):
    news_item = News.objects.alL()
    ctx = {
        'news_item': news_item
    }
    return render(request, 'dashboard/news/list.html', ctx)


def news_create(request):
    model = News()
    form = NewsForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('news_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_edit(request, pk):
    model = News.objects.get(pk=pk)
    form = NewsForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('news_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_delete(request, pk):
    model = News.objects.get(pk=pk)
    model.delete()
    return redirect('news_list')


# ================= Courses =================
def courses_list(request):
    courses = Course.objects.alL()
    ctx = {
        'courses': courses
    }
    return render(request, 'dashboard/course/list.html', ctx)


def courses_create(request):
    model = Course()
    form = CourseForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('courses_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/course/form.html', ctx)


def courses_edit(request, pk):
    model = Course.objects.get(pk=pk)
    form = CourseForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('courses_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/course/form.html', ctx)


def courses_delete(request, pk):
    model = News.objects.get(pk=pk)
    model.delete()
    return redirect('courses_list')


# ================= Lessons =================
def lessons_list(request):
    lessons = Lesson.objects.alL()
    ctx = {
        'lessons': lessons
    }
    return render(request, 'dashboard/lesson/list.html', ctx)


def lessons_create(request):
    model = Lesson()
    form = LessonForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('lessons_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/lesson/form.html', ctx)


def lessons_edit(request, pk):
    model = Lesson.objects.get(pk=pk)
    form = LessonForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('lessons_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/lesson/form.html', ctx)


def lessons_delete(request, pk):
    model = Lesson.objects.get(pk=pk)
    model.delete()
    return redirect('lessons_list')
