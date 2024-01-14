from rest_framework import serializers

from .models import Todo
#from login.serializers import UserPublicSerializer


class TodoSerializer(serializers.ModelSerializer):
    #owner = UserPublicSerializer(source='user', read_only=True)
    #my_user_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Todo
        #fields = ['title', 'description', 'status', 'my_user_data']
        fields = ['id', 'title', 'description', 'status']

    # def get_my_user_data(self, obj):
    #     return {
    #         "username": obj.user.username
    #     }
