from django.shortcuts import render
from core.models import AboutUs, News, Lesson, Course, MainPhoto, Teacher


def home_page(request):
    about_us = AboutUs.objects.all()
    news_item = News.objects.order_by('-created_at')[:6]
    courses = Course.objects.count()
    lessons = Lesson.objects.count()
    teachers = Teacher.objects.count()

    ctx = {
        'courses_count': courses,
        'teachers_count': teachers,
        'lessons_count': lessons,
    }

    return render(request, 'core/index.html', ctx)
