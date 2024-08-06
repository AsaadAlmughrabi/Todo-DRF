from django.contrib import admin
from django.urls import path

from .views import TodoListView,TodoDetailView

urlpatterns = [
    path('',TodoListView.as_view(),name='home'),
    path('<int:pk>',TodoDetailView.as_view(),name='todo_detail'),
    
]
