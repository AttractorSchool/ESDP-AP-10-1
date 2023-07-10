from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from accounts.views.authentification import CookieJWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

from webapp.models import Events


class NewslineView(ListView):
    model = Events
    template_name = 'newsline.html'
    context_object_name = 'events'
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        authenticator = self.authentication_classes[0]()

        try:
            user_auth_tuple = authenticator.authenticate(request)
        except AuthenticationFailed:
            return HttpResponseRedirect(reverse('login'))
        else:
            if user_auth_tuple:
                print(user_auth_tuple)
                request.user, request.auth = user_auth_tuple
            else:
                return HttpResponseRedirect(reverse('login'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        print(self.request.user)
        context = super().get_context_data(**kwargs)
        context['events'] = Events.objects.all().exclude(is_deleted=True).order_by('-created_at')
        context['user_obj'] = self.request.user
        return context
