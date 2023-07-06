from django.utils.deprecation import MiddlewareMixin

from accounts.cookie_auth import CookieJWTAuthentication


class CookieJWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth = CookieJWTAuthentication()
        auth_result = auth.authenticate(request)
        if auth_result is not None:
            auth_user, _ = auth_result
            if auth_user is not None:
                request.user = auth_user
