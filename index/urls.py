# the urls.py for index

from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.user_login, name='login'),

    path('register/', views.register, name='register'),
]