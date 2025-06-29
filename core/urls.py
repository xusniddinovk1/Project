from django.urls import path
from core.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('courses/<int:id>', course_detail, name='course_detail'),
]
