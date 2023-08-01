from django.contrib import admin
from django.urls import path
from .views import emailview

urlpatterns = [
    path('', emailview, name="contact"),
    ]