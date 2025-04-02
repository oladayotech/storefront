from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('hello2/', views.say_hello2, name='hello'),
]