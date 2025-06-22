from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('sign-up/', signup_page, name='signup_page'),
    path('logout/', logout_page, name='logout_page'),

    path('about-us/', about_us_list, name='about_us_list'),
    path('about-us/create/', about_us_create, name='about_us_create'),
    path('about-us/<slug:slug>/edit/', about_us_edit, name='about_us_edit'),
    path('about-us/<slug:slug>/delete/', about_us_delete, name='about_us_delete'),

    path('news/', news_list, name='news_list'),
    path('news/create/', news_create, name='news_create'),
    path('news/<slug:slug>/edit/', news_edit, name='news_edit'),
    path('news/<slug:slug>/delete/', news_delete, name='news_delete'),

    path('courses/', courses_list, name='courses_list'),
    path('courses/create/', courses_create, name='courses_create'),
    path('courses/<slug:slug>/edit/', courses_edit, name='courses_edit'),
    path('courses/<slug:slug>/delete/', courses_delete, name='courses_delete'),

    path('lessons/', lessons_list, name='lessons_list'),
    path('lessons/create/', lessons_create, name='lessons_create'),
    path('lessons/<slug:slug>/edit/', lessons_edit, name='lessons_edit'),
    path('lessons/<slug:slug>/delete/', lessons_delete, name='lessons_delete'),

]
