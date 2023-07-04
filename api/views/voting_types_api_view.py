import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api.serializers import VotingTypesSerializer
from webapp.models import VotingTypes, NameVotingTypes, Vote


class VotingTypesSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = VotingTypes.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Голосования отсутствуют"})
        else:
            serializer = VotingTypesSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            data['voting_type'] = NameVotingTypes.objects.get(id=data.get('voting_type'))
            data['vote'] = Vote.objects.get(id=data.get('vote'))
            vote = VotingTypes.objects.create(**data)
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class VotingTypesApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(VotingTypes, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = VotingTypesSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(VotingTypes, pk=kwargs.get("pk"))
        serializer = VotingTypesSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(VotingTypes, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
