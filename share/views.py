from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ShareSerializer, ShareSerializerGet
from .models import Share
from rest_framework.response import Response
from rest_framework import status
from user.models import User


class ShareView(APIView):
    @staticmethod
    def get(self):
        data = Share.objects.all().prefetch_related('post', 'post__post_content')

        serializer = ShareSerializerGet(data, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print(data)

        serializer = ShareSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        else:
            print("jjjj", serializer.errors)

        return Response(status.HTTP_200_OK)
