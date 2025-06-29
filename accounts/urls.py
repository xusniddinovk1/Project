from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', index_page, name='index_page'),

    path('register', register_page, name='register_page'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
