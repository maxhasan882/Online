from rest_framework import serializers
from .models import Share
from timeline.serializers import PostSerializerGet
from user.serializers import UserSerializer


class ShareSerializerGet(serializers.ModelSerializer):
    post = PostSerializerGet(read_only=True)
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Share
        fields = ['post']


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'
