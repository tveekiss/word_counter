from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load, name='load'),
    path('wordcount/', views.wordcount, name='wordcount'),
    path('clear/', views.clear, name='clear'),
]