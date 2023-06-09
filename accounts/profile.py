from django.contrib.auth import get_user_model
from django.views.generic import DetailView


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'


