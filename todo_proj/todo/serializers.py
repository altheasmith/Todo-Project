from todo.models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'task', 'owner', 'due_date', 'completed', 'create_date')
