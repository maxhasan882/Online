from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'is_superuser', 'is_staff', 'is_active', 'profile_pic', 'cover_photo', 'dob',
                  'address')


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)
    profile_pic = serializers.FileField(allow_null=True, required=False, allow_empty_file=True)
    cover_photo = serializers.FileField(allow_null=True, required=False, allow_empty_file=True)
    dob = serializers.DateTimeField(allow_null=True)
    address = serializers.CharField(max_length=100, allow_null=True, required=False, allow_blank=True)

    def create(self, validated_data):
        print("User valid data: ", validated_data)
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        user.name = validated_data['name']
        user.code = validated_data['code']
        user.profile_pic = validated_data['profile_pic']
        user.cover_photo = validated_data['cover_photo']
        user.dob = validated_data['dob']
        user.address = validated_data['address']
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'code', 'profile_pic', 'cover_photo', 'dob', 'address')


class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()