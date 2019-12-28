from rest_framework import serializers
from .models import Friend, Follow, Block, FriendRequest
from user.serializers import UserSerializer, UserCreateSerializer


class FriendSerializer(serializers.ModelSerializer):
    who = UserCreateSerializer()
    whom = UserSerializer()

    class Meta:
        model = Friend
        fields = ('who', 'whom', 'date')


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
