from rest_framework import generics, permissions

from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permissions_classes = permissions.IsAuthenticated

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('description') or None
        if content is None:
            content = title
        serializer.save(description=content)


todo_list_create_view = TodoListCreateAPIView.as_view()


class TodoDetailAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permissions_classes = permissions.IsAuthenticated


todo_detail_view = TodoDetailAPIView.as_view()


class TodoDestroyAPIView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    permissions_classes = permissions.IsAuthenticated

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


todo_destroy_view = TodoDestroyAPIView.as_view()
