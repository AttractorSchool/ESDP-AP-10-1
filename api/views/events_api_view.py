from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api.serializers import EventsSerializer
from webapp.models import Events


class EventsSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = Events.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = EventsSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)





