from django.views.generic import ListView

from webapp.models import Events


class NewslineView(ListView):
    model = Events
    template_name = 'newsline.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')


