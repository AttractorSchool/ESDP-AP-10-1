from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.serializers import UserSerializer, LoginSerializer


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
    permission_classes = [AllowAny]

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
        response.set_cookie(key='jwt', value=str(refresh.access_token), httponly=True, secure=False)
        response.set_cookie(key='refresh_jwt', value=str(refresh), httponly=True, secure=False)
        return response

    def get(self, request):
        return render(request, 'login.html')


class LogoutUserView(APIView):
    def post(self, request):
        response = Response({"detail": "Logout Successful"}, status=status.HTTP_200_OK)
        response.delete_cookie('jwt')
        response.delete_cookie('refresh_jwt')
        return response


class CheckAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"authenticated": True})
