from django.shortcuts import render
from core.models import AboutUs, News, Lesson, Course, MainPhoto, Teacher


def about_us_view(request):
    about_list = AboutUs.objects.all()
    return render(request, 'core/about.html', {'about_list': about_list})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/teachers.html', {'teachers': teachers})
