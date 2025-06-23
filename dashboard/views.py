from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from core.models import AboutUs, News, Course, Lesson
from dashboard.forms import AboutUsForm, NewsForm, CourseForm, LessonForm, ProfileForm
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
def my_profile(request):
    ctx = {
        'user': request.user,
    }
    return render(request, 'dashboard/profile/profile.html', ctx)

@login_required_decorator
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_profile')  # profil sahifasiga qaytish
    else:
        form = ProfileForm(instance=user)

    ctx = {
        'form': form
    }

    return render(request, 'dashboard/profile/profile_edit.html', ctx)


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'dashboard/profile/password_change.html'
    success_url = reverse_lazy('password_change_done')

@login_required_decorator
def home_page(request):
    users = User.objects.all()
    news = News.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()

    items = [
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": users.count(),
            "label": "Users",
            "chart_data": [users.count(), users.count() // 2, users.count() // 3]
        },
        {
            "icon": "fa-book",
            "color": "#10b981",  # green-500
            "count": news.count(),
            "label": "News",
            "chart_data": [news.count(), news.count() // 2, news.count() // 3]
        },
        {
            "icon": "fa-bell",
            "color": "#ef4444",  # red-500
            "count": courses.count(),
            "label": "Courses",
            "chart_data": [courses.count(), courses.count() // 2, courses.count() // 3]
        },
        {
            "icon": "fa-star",
            "color": "#facc15",  # yellow-500
            "count": lessons.count(),
            "label": "Lessons",
            "chart_data": [lessons.count(), lessons.count() // 2, lessons.count() // 3]
        },
    ]
    return render(request, 'dashboard/index.html', {'items': items})


# ================= News =================
def about_us_list(request):
    text = AboutUs.objects.all()
    ctx = {
        'text': text
    }
    return render(request, 'dashboard/about_us/list.html', ctx)


def about_us_create(request):
    model = AboutUs()
    form = AboutUsForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('about_us_list')
    ctx = {
        'model': model,
        'form': form,
    }
    return render(request, 'dashboard/about_us/form.html', ctx)


def about_us_edit(request, slug):
    model = AboutUs.objects.get(slug=slug)
    form = AboutUsForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('about_us_list')
    ctx = {
        'model': model,
        'form': form,
    }
    return render(request, 'dashboard/about_us/form.html', ctx)


def about_us_delete(request, slug):
    model = AboutUs.objects.get(slug=slug)
    model.delete()
    return redirect('about_us_list')


# ================= News =================
def news_list(request):
    news_item = News.objects.all()
    ctx = {
        'news_item': news_item
    }
    return render(request, 'dashboard/news/list.html', ctx)


def news_create(request):
    model = News()
    form = NewsForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('news_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_edit(request, slug):
    model = News.objects.get(slug=slug)
    form = NewsForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('news_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_delete(request, slug):
    model = News.objects.get(slug=slug)
    model.delete()
    return redirect('news_list')


# ================= Courses =================
def courses_list(request):
    courses = Course.objects.all()
    ctx = {
        'courses': courses
    }
    return render(request, 'dashboard/course/list.html', ctx)


def courses_create(request):
    model = Course()
    form = CourseForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('courses_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/course/form.html', ctx)


def courses_edit(request, slug):
    model = Course.objects.get(slug=slug)
    form = CourseForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('courses_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/course/form.html', ctx)


def courses_delete(request, slug):
    model = News.objects.get(slug=slug)
    model.delete()
    return redirect('courses_list')


# ================= Lessons =================
def lessons_list(request):
    lessons = Lesson.objects.all()
    ctx = {
        'lessons': lessons
    }
    return render(request, 'dashboard/lesson/list.html', ctx)


def lessons_create(request):
    model = Lesson()
    form = LessonForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('lessons_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/lesson/form.html', ctx)


def lessons_edit(request, slug):
    model = Lesson.objects.get(slug=slug)
    form = LessonForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('lessons_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/lesson/form.html', ctx)


def lessons_delete(request, slug):
    model = Lesson.objects.get(slug=slug)
    model.delete()
    return redirect('lessons_list')
