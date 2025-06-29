from django.shortcuts import render
from core.models import AboutUs, News, Lesson, Course, MainPhoto, Teacher


def home_page(request):
    about_us = AboutUs.objects.all()
    news_item = News.objects.order_by('-created_at')[:6]
    courses = Course.objects.all()[:6]
    lessons = Lesson.objects.all()[:6]
    teachers = Teacher.objects.all()[:8]
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


def course_detail(request, id):
    course = Course.objects.get(pk=id)

    related_courses = Course.objects.order_by('-created_at')[:6]

    ctx = {
        'course': course,
        'related_courses': related_courses
    }
    return render(request, 'core/course/course_detail.html', ctx)
