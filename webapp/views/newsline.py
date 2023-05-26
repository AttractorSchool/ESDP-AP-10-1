from django.views.generic import TemplateView
from webapp.models import Events, News

class NewslineView(TemplateView):
    template_name = 'newsline.html'

    def get_context_data(self, **kwargs):
        context = {}
        events = Events.objects.all().order_by('created_at')
        news = News.objects.all().order_by('created_at')
        all_news = []
        for event in events:
            event.type = 'Event'
            all_news.append(event)
        for news_alone in news:
            news_alone.type = 'News'
            all_news.append(news_alone)
        for i in range(len(all_news)):
            for j in range(len(all_news)):
                if all_news[i].created_at > all_news[j].created_at:
                    all_news[i], all_news[j] = all_news[j], all_news[i]
        context['newsline'] = all_news
        return context
