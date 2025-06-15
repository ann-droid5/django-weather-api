# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #path('register/', views.register_api, name='register_api'),
    #path('login/', views.login_api, name='login_api'),

    path('register/', views.register_page),
    path('login/', views.login_page),
    path('home/', views.home_page),
    path('logout/', views.logout_page),
]
