from django.views.generic import TemplateView


class NewslineView(TemplateView):
    template_name = 'newsline.html'
