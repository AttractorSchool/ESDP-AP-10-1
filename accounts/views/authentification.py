from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raw_token = request.COOKIES.get('jwt')
            if raw_token is None:
                return None
            validated_token = self.get_validated_token(raw_token)
            user_id = validated_token.get("user_id")
            User = get_user_model()
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return None
            return (user, validated_token)
        return super().authenticate(request)


class RegisterUserView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                refresh = RefreshToken.for_user(user)
                res = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
        }
        response = Response(res, status=status.HTTP_200_OK)
        response.set_cookie(key='jwt', value=str(refresh.access_token), httponly=True)
        return response

    def get(self, request):
        return render(request, 'login.html')
