from todo.serializers import TodoSerializer
from todo.models import Todo
from rest_framework import viewsets


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
