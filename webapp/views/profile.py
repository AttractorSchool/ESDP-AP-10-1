from django.views.generic import ListView, DetailView
from rest_framework.permissions import IsAuthenticated

from accounts.models import Account
from accounts.cookie_auth import CookieJWTAuthentication


class ProfileListView(ListView):
    model = Account
    template_name = 'profile_list_django.html'
    context_object_name = 'accounts'
    authentication_classes = [CookieJWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user_account = self.request.user
        queryset = super().get_queryset().exclude(pk=user_account.pk)
        queryset = queryset.order_by('-pk')
        queryset = [user_account] + list(queryset)
        return queryset


class ProfileDetailView(DetailView):
    model = Account
    template_name = 'profile_detail.html'
    context_object_name = 'account'
