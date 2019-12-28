from rest_framework import serializers
from general.models import Rating
from timeline.serializers import PostSerializer, PostSerializerGet
from user.serializers import UserSerializer


class RatingSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['user', 'post', 'rate']
