from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ImageSerializer
from webapp.models import  Image


class PhotoSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            cities = Image.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = ImageSerializer(cities, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)