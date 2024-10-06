from rest_framework import serializers
from task.models import ToDoTask


class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = ["title", "created", "category", "description"]
