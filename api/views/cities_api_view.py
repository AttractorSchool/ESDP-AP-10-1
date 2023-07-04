from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CitiesSerializer
from webapp.models import Cities


class CitiesSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            cities = Cities.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = CitiesSerializer(cities, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
