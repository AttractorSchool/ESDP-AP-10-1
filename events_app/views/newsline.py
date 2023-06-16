from django.views.generic import TemplateView
from events_app.models import Events, News


class NewslineView(TemplateView):
    template_name = 'newsline.html'
