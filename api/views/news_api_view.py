from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import NewsSerializer
from events_app.models import News


class NewsSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = News.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Новости отсутствуют"})
        else:
            serializer = NewsSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
