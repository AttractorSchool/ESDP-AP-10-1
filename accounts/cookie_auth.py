from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        print(f'Header: {header}')
        if header is None:
            raw_token = request.COOKIES.get('jwt')
            print(f'Raw token from Cookie: {raw_token}')
            if raw_token is None:
                return None
            try:
                validated_token = self.get_validated_token(raw_token)
            except TokenError as e:
                if isinstance(e, InvalidToken):
                    print("Access token is expired.")
                    return None
                else:
                    return None
            print(f'Validated Token: {validated_token}')
            user_id = validated_token.get("user_id")
            User = get_user_model()
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return None
            return (user, validated_token)
        return super().authenticate(request)
