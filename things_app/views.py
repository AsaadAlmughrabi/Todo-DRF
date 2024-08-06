from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import isOwnerOrReadOnly
# Create your views here.

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [isOwnerOrReadOnly]

