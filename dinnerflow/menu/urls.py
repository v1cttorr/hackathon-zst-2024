from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('add_meal/', add_meal, name="add_meal"),
    path('edit_meal/<int:id>/', edit_meal, name="edit_meal"),
]
