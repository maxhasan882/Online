from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import UserCreateSerializer, UserSerializer, CustomTokenSerializer
from rest_framework.views import Response
from rest_framework import status, exceptions
from django.db import transaction
from django.db import connection
from .models import User
from worker import UserWorker
from signals.passwordreset import send_email
import requests
import django_rest_passwordreset.views
from django_rest_passwordreset.serializers import PasswordTokenSerializer
from django_rest_passwordreset.models import get_password_reset_token_expiry_time, ResetPasswordToken


class UserCreateView(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        print('Data is: ', data)
        code = UserWorker.get_user_code(data['name'][0])
        date = None if data['dob'] == '' else data['dob']
        new_user = {'email': data['email'], 'name': data['name'], 'password': data['password'], 'code': code,
                    'profile_pic': request.data.get('profile_pic'), 'cover_photo': request.data.get('cover_photo'),
                    'dob': date, 'address': data['address']}
        serializer = UserCreateSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            send_email.send(sender=User, email=str(request.data["email"]), content=new_user["name"])
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @transaction.atomic
    def patch(request):
        data = request.data
        user = get_object_or_404(User, pk=request.user.id)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PassWordReset(APIView):
    def get(self, request):
        data = request.GET.get('token')
        print(data)
        serializer = CustomTokenSerializer(data={'token': data})
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']
        print("Token is: ", token)
        password_reset_token_validation_time = get_password_reset_token_expiry_time()
        reset_password_token = ResetPasswordToken.objects.filter(key=token).first()
        if reset_password_token is None:
            return Response({'status': 'notfound'}, status=status.HTTP_404_NOT_FOUND)
        expiry_date = reset_password_token.created_at + timedelta(hours=password_reset_token_validation_time)

        if timezone.now() > expiry_date:
            reset_password_token.delete()
            return Response({'status': 'expired'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'status': 'OK', 'token': token}) #redirect to a front end link


class ResetPasswordConfirm(GenericAPIView):
    throttle_classes = ()
    permission_classes = ()
    serializer_class = PasswordTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        token = serializer.validated_data['token']
        password_reset_token_validation_time = get_password_reset_token_expiry_time()
        reset_password_token = ResetPasswordToken.objects.filter(key=token).first()

        if reset_password_token is None:
            return Response({'status': 'notfound'}, status=status.HTTP_404_NOT_FOUND)
        expiry_date = reset_password_token.created_at + timedelta(hours=password_reset_token_validation_time)

        if timezone.now() > expiry_date:
            reset_password_token.delete()
            return Response({'status': 'expired'}, status=status.HTTP_404_NOT_FOUND)
        try:
            validate_password(
                password,
                user=reset_password_token.user,
                password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
            )
        except ValidationError as e:
            raise exceptions.ValidationError({
                'password': e.messages
            })

        reset_password_token.user.set_password(password)
        reset_password_token.user.save()
        ResetPasswordToken.objects.filter(user=reset_password_token.user).delete()
        return Response({'status': 'OK'})