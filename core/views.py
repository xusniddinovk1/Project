from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from bs4 import BeautifulSoup  # ✅ kerakli import
from core.models import News, Lesson, Course, Teacher


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


def news_page(request):
    news_item = News.objects.all()
    ctx = {
        'news_item': news_item
    }
    return render(request, 'core/news/news.html', ctx)


def news_detail_page(request, slug):
    news = get_object_or_404(News, slug=slug)

    # Content ichidagi sarlavhalardan mundarija yasash
    soup = BeautifulSoup(news.content, 'html.parser')
    headings = soup.find_all(['h2', 'h3'])

    toc = []
    for tag in headings:
        title = tag.get_text()
        id_attr = slugify(title)  # har bir heading uchun id
        tag['id'] = id_attr  # id atributini qo‘shish
        toc.append({'title': title, 'id': id_attr, 'tag': tag.name})

    news.content = str(soup)  # ID qo‘shilgan contentni yangilaymiz

    context = {
        'news': news,
        'toc': toc,
    }
    return render(request, 'core/news/news_detail.html', context)
