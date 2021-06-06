from django.contrib import admin
from django.urls import path,include
from .views import IMSCR,description
urlpatterns = [
    path('',IMSCR),
    path('about',description)
]
