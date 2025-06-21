from django.shortcuts import render, redirect
from core.models import AboutUs, News, Course, Lesson
from dashboard.forms import AboutUsForm, NewsForm, CourseForm, LessonForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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
