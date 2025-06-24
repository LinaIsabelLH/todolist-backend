from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class= CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-created_at')
    serializer_class= TaskSerializer

    def get_queryset(self):
        category_id= self.request.query_params.get('category_id')
        if category_id:
            return self.queryset.filter(category_id=category_id)
        return self.queryset



