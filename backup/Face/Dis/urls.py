from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('go',views.go,name='go'),
    path('',views.index,name='index'),
]