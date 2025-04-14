from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('birds/', views.bird_list, name='bird_list'),
    path('add/', views.add_bird, name='add_bird'),
    path('quiz/', views.quiz, name='quiz'),
]
