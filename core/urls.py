from django.urls import path
from core.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
]
