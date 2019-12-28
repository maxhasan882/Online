from rest_framework import serializers
from .models import Content
from timeline.serializers import PostSerializer
from generic_relations.relations import GenericRelatedField
from timeline.models import Post


class ContentSerializerPost(serializers.ModelSerializer):
    content_object = GenericRelatedField({
        Post: PostSerializer()
    })

    class Meta:
        model = Content
        fields = ['content_object', 'album', 'user', 'file']


class ContentSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['album', 'user', 'file']