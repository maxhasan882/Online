from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response
from general.models import Rating
from general.serializers import RatingSerializer


class RatingView(APIView):
    @staticmethod
    def get(self):
        data = Rating.objects.all()

        serializer = RatingSerializer(data, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        return Response(status.HTTP_200_OK)