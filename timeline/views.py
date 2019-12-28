from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.db import transaction
from .serializers import PostSerializer, PostSerializerGet
from django.contrib.contenttypes.models import ContentType
from .models import Album, Post
from content.models import Content
from psycopg2._psycopg import IntegrityError
from rest_framework.response import Response
from rest_framework import status


class PostView(APIView):
    @staticmethod
    def get(request):
        posts = Post.objects.all().prefetch_related('post_content')
        serialize = PostSerializerGet(posts, many=True)
        return Response(serialize.data, status=status.HTTP_202_ACCEPTED)

    @transaction.atomic
    def post(self, request):
        try:
            data = request.data
            post_data = {'post_text': data['post_text'], 'user': request.user.id,
                         'visibility_mode': data['visibility_mode']}
            serializer = PostSerializer(data=post_data)
            if serializer.is_valid():
                post = serializer.save()
                files = request.data.getlist('content')
                album = Album.objects.get_or_create(name='Your Photos', user=request.user)
                if files:
                    for file in files:
                        Content.objects.create(content_object=post, file=file,
                                               album=album[0], user=request.user)
                    return Response(status=status.HTTP_201_CREATED)
            raise PermissionDenied('Save Error')
        except IntegrityError as e:
            raise PermissionDenied(e)
