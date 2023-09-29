from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from todo.models import Todo, TodoList
from todo.serializers import TodoListSerializer, TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['due_date', 'favourite', "completed", "list"]
    search_fields = ["title"]


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
