from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerGet(serializers.ModelSerializer):
    from content.serializers import ContentSerializerPost, ContentSerializerGet
    from user.serializers import UserSerializer
    user = UserSerializer()
    post_content = ContentSerializerGet(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['post_text', 'date_time', 'user', 'post_content']