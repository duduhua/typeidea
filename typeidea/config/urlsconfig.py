from django.contrib import admin
from django.urls import path, include

from .views import LinkListView

urlpatterns = [
    path('', LinkListView.as_view(), name='links'),
]