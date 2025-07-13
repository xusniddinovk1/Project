from django.urls import path
from core.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('success/', success_view, name='success'),
    path('news/', news_page, name='news_page'),
    path('news/<slug:slug>', news_detail_page, name='news_detail_page'),
]
