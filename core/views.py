from django.shortcuts import render
from core.models import AboutUs, News, Lesson, Course, MainPhoto, Teacher
from dashboard.views import about_us_edit


def home_page(request):
    about_us = AboutUs.objects.all()
    news_item = News.objects.order_by('-created_at')[:6]
    courses = Course.objects.all()
    lessons = Lesson.objects.all()[:8]
    teachers = Teacher.objects.all()
    main_photo = MainPhoto.objects.last()

    ctx = {
        'about_us': about_us,
        'news_items': news_item,
        'courses': courses,
        'lessons': lessons,
        'teachers': teachers,
        'main_photo': main_photo
    }
    return render(request, 'core/index.html', ctx)
