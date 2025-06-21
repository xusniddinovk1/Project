from django.shortcuts import render, redirect
from dashboard.forms import AboutUsForm, NewsForm, CourseForm, LessonForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.POST:
        phone_number = request.POST.get('phone_number', None)
        password = request.POST.get('password', None)
        user = authenticate(phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')
