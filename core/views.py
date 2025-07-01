from django.shortcuts import render
from core.models import AboutUs, News, Lesson, Course, MainPhoto, Teacher


def home_page(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    teachers = Teacher.objects.all()

    ctx = {
        'courses': courses,
        'courses_count': len(courses),
        'teachers_count': len(teachers),
        'lessons_count': len(lessons),
    }

    return render(request, 'core/index.html', ctx)
