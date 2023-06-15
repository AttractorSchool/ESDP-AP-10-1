from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.views.generic import DetailView


class ProfileListView(TemplateView):
    template_name = 'profile_list_view.html'
    ordering = ["created_at"]

class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'




