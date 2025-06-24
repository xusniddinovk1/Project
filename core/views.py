from django.shortcuts import render
from core.models import AboutUs, News, Lesson, Course, MainPhoto


def home_page(request):
    about = AboutUs.objects.all()
    news_list = News.objects.order_by('-created_at')[:3]
    courses = Course.objects.order_by('-created_at')[:3]
    lessons = Lesson.objects.order_by('-created_at')[:3]

    context = {
        'about': about,
        'news_list': news_list,
        'courses': courses,
        'lessons': lessons
    }

    return render(request, 'core/index.html', context)


def main_photo(request):
    photo = MainPhoto.objects.first()
    ctx = {
        'photo': photo
    }
    return render(request, 'core/index.html', ctx)