from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import isOwnerOrReadOnly

# Create your views here.

import logging

logger = logging.getLogger(__name__)


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        logger.debug("Entering TodoListView list method")
        response = super().list(request, *args, **kwargs)
        logger.debug("Exiting TodoListView list method")
        return response

    def create(self, request, *args, **kwargs):
        logger.debug("Entering TodoListView create method")
        response = super().create(request, *args, **kwargs)
        logger.debug("Exiting TodoListView create method")
        return response


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [isOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        logger.debug("Entering TodoDetailView retrieve method")
        response = super().retrieve(request, *args, **kwargs)
        logger.debug("Exiting TodoDetailView retrieve method")
        return response

    def update(self, request, *args, **kwargs):
        logger.debug("Entering TodoDetailView update method")
        response = super().update(request, *args, **kwargs)
        logger.debug("Exiting TodoDetailView update method")
        return response

    def destroy(self, request, *args, **kwargs):
        logger.debug("Entering TodoDetailView destroy method")
        response = super().destroy(request, *args, **kwargs)
        logger.debug("Exiting TodoDetailView destroy method")
        return response
