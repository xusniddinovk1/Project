from django.urls import path
from core.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('news/', news_page, name='news_page'),
    path('news/<slug:slug>', news_detail_page, name='news_detail_page'),
]
