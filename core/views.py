import os
import requests
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from bs4 import BeautifulSoup  # ✅ kerakli import
from dotenv import load_dotenv

from accounts.forms import ContactForm
from core.models import News, Lesson, Course, Teacher

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')


def home_page(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            username = form.cleaned_data['username']

            # send message to telegram admin
            message = f"🆕 Yangi murojaat:\n👤 Ismi: {name}\n📞 Telefon: {phone_number}\n💬 Telegram: {username}"
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": ADMIN_ID, "text": message})

            return redirect('success')  # yoki xuddi shu sahifaga qaytarish
    else:
        form = ContactForm()

    ctx = {
        'courses': courses,
        'courses_count': len(courses),
        'teachers_count': len(teachers),
        'lessons_count': len(lessons),
        'form': form
    }

    return render(request, 'core/index.html', ctx)


def success_view(request):
    return HttpResponse("Ma'lumot muvaffaqiyatli jo‘natildi!")


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
