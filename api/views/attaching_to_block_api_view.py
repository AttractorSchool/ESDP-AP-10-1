import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from accounts.models import Account
from api.serializers import AttachingToBlockSerializer
from webapp.models import ListVotes, Events, News, AttachingToBlock


class AttachingToBlockSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = AttachingToBlock.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Голосования отсутствуют"})
        else:
            serializer = AttachingToBlockSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            data['list_of_votes'] = ListVotes.objects.get(id=data.get('list_of_votes'))
            data['events'] = Events.objects.get(id=data.get('events'))
            data['news'] = News.objects.get(id=data.get('news'))
            data['users'] = Account.objects.get(id=data.get('users'))
            vote = AttachingToBlock.objects.create(**data)
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class AttachingToBlockApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(AttachingToBlock, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = AttachingToBlockSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(AttachingToBlock, pk=kwargs.get("pk"))
        serializer = AttachingToBlockSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(AttachingToBlock, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
