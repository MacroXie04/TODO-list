# the urls.py for index

from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.user_login, name='login'),

    path('register/', views.register, name='register'),

    path('complete/<int:item_id>/', views.complete_todo, name='complete_todo'),

    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),

    path('logout/', views.web_logout, name='logout'),
]