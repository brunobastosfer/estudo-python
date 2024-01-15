from rest_framework import generics, permissions

from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('description') or None
        user = serializer.validated_data.get('user')
        if content is None:
            content = title
        serializer.save(description=content, owner=self.request.user)


todo_list_create_view = TodoListCreateAPIView.as_view()


class TodoDetailAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permissions_classes = permissions.IsAuthenticated


todo_detail_view = TodoDetailAPIView.as_view()


class TodoUpdateAPIView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.title:
            instance.content = instance.title


todo_update_view = TodoUpdateAPIView.as_view()


class TodoDestroyAPIView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    permission_classes = (permissions.IsAuthenticated, )

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


todo_destroy_view = TodoDestroyAPIView.as_view()
