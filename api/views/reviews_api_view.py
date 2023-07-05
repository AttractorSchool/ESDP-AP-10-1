from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.utils import json
from accounts.models import Review, Account
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

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            data['user_write_review'] = Account.objects.get(id=data.get('user_write_review'))
            data['user_receive_review'] = Account.objects.get(id=data.get('user_receive_review'))
            reviews = Review.objects.create(**data)
            return Response({"create": "Успешно создан"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response



class ReviewApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Review, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = ReviewsSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(Review, pk=kwargs.get("pk"))
        serializer = ReviewsSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Review, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delete - {kwargs.get('pk')}": "Мягкое удаление выполнено успешно"})

