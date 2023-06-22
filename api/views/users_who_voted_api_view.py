import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from accounts.models import Account
from api.serializers import UsersWhoVotedSerializer
from webapp.models import UsersWhoVoted, VotingOptions


class UsersWhoVotedSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = UsersWhoVoted.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Голосования отсутствуют"})
        else:
            serializer = UsersWhoVotedSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            data['possible_answer'] = VotingOptions.objects.get(id=data.get('possible_answer'))
            data['users'] = Account.objects.get(id=data.get('users'))
            vote = UsersWhoVoted.objects.create(**data)
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class UsersWhoVotedApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(UsersWhoVoted, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = UsersWhoVotedSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(UsersWhoVoted, pk=kwargs.get("pk"))
        serializer = UsersWhoVotedSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(UsersWhoVoted, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
