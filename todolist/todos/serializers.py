from rest_framework import serializers

from .models import Todo
from login.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'owner']
