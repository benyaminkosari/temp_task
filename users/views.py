from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .mixin import BaseResponseMixin
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class RegisterView(APIView, BaseResponseMixin):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = self.create_user(request.data)
        self.create_token(user)
        return self.custom_response("Registered successfully", {'username': user.username,
                                                                        'email': user.email},
                                    status=status.HTTP_201_CREATED)

    def create_user(self, data):
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return user

    def create_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token


class LoginView(ObtainAuthToken, BaseResponseMixin):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return self.custom_response("Login successfully", response.data, status=status.HTTP_200_OK)
