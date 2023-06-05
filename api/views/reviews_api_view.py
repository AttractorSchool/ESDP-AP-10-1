from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Review
from api.serializers import ReviewsSerializer


class ReviewsSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = Review.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Отзывы отсутствуют"})
        else:
            serializer = ReviewsSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
