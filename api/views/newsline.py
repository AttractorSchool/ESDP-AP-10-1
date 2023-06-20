from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import EventsSerializer, NewsSerializer
from webapp.models import Events, News
from rest_framework.permissions import IsAuthenticated

class NewslineApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        events = Events.objects.all().order_by('created_at')
        news = News.objects.all().order_by('created_at')
        all_news = []
        serializer_news = NewsSerializer(news, many=True).data
        serializer_events = EventsSerializer(events, many=True).data
        for event in serializer_events:
            all_news.append(event)
        for news_alone in serializer_news:
            all_news.append(news_alone)
        for i in range(len(all_news)):
            for j in range(len(all_news)):
                if all_news[i]["created_at"] > all_news[j]["created_at"]:
                    all_news[i], all_news[j] = all_news[j], all_news[i]
        return Response(all_news, status=status.HTTP_200_OK)
