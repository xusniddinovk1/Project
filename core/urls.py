from django.urls import path
from core.views import *

urlpatterns = [
    path('', about_us_view, name='home_page'),
]
