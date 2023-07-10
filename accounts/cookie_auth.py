from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        print(f'Header: {header}')
        if header is None:
            raw_access_token = request.COOKIES.get('jwt')
            raw_refresh_token = request.COOKIES.get('refresh_jwt')
            print(f'Raw Access Token: {raw_access_token}')
            print(f'Raw Refresh Token: {raw_refresh_token}')
            if raw_access_token is None:
                return None
            try:
                validated_token = self.get_validated_token(raw_access_token)
                print(f'Validated Token: {validated_token}')
            except TokenError as e:
                if isinstance(e, InvalidToken) and raw_refresh_token is not None:
                    try:
                        RefreshToken(raw_refresh_token).check_blacklist()
                        validated_token = RefreshToken(raw_refresh_token).access_token

                        user_id = validated_token.get("user_id")
                        User = get_user_model()
                        try:
                            user = User.objects.get(id=user_id)
                        except User.DoesNotExist:
                            return None
                        return user, validated_token
                    except TokenError:
                        return None
                return None
            user_id = validated_token.get("user_id")
            User = get_user_model()
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return None
            return user, validated_token
        return super().authenticate(request)
