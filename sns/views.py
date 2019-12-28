from django.shortcuts import render
from rest_framework.views import APIView
from .models import Friend
from .serializers import FriendSerializer, FriendRequestSerializer
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist


class FriendListView(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request):
        try:
            friends = Friend.objects.all().filter(pk=request.user.id)
            serializer = FriendSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            Response(status=status.HTTP_204_NO_CONTENT)


class FriendRequestView(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def post(request):
        data = request.data
        if request.user.id == int(data['who']):
            serializer = FriendRequestSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "Friend has been Request sent"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "Unknown"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
