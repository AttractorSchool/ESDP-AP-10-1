from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from accounts.cookie_auth import CookieJWTAuthentication


class CookieJWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("CookieJWTAuthenticationMiddleware has been called")
        if request.path != reverse('login'):
            auth = CookieJWTAuthentication()
            try:
                auth_result = auth.authenticate(request)
            except InvalidToken:
                print("Token is invalid or expired. Redirecting to login page.")
                return redirect('login')

            if auth_result is not None:
                auth_user, _ = auth_result
                if auth_user is not None:
                    request.user = auth_user


class JWTRefreshTokenMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        print("JWTRefreshTokenMiddleware has been called")
        if request.path != reverse('login'):
            auth = CookieJWTAuthentication()
            try:
                auth_result = auth.authenticate(request)
            except InvalidToken:
                print("Access token is invalid or expired. Trying to refresh using refresh token.")
                raw_refresh_token = request.COOKIES.get('refresh_jwt')
                if raw_refresh_token is not None:
                    try:
                        print(f"Raw refresh token: {raw_refresh_token}")
                        refresh = RefreshToken(raw_refresh_token)
                        new_tokens = refresh.access_token
                        response.set_cookie(key='jwt', value=str(new_tokens), httponly=True, secure=False)
                        response.set_cookie(key='refresh_jwt', value=str(refresh), httponly=True, secure=False)
                    except TokenError as e:
                        print(f"Error while refreshing tokens: {str(e)}")
                        print(f"Raw refresh token: {raw_refresh_token}")
                        if isinstance(e, InvalidToken):
                            print("Refresh token is invalid. Redirecting to login page.")
                            return redirect('login')
                        else:
                            print(f"Error while refreshing tokens: {str(e)}")
            else:
                if auth_result is not None:
                    auth_user, _ = auth_result
                    if auth_user is not None:
                        request.user = auth_user
        return response
