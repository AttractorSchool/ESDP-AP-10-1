import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from accounts.models import Account
from api.serializers import ListVotesSerializer
from webapp.models import ListVotes, Vote


class ListVotesSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = ListVotes.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Голосования отсутствуют"})
        else:
            serializer = ListVotesSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            vote_list = data.get('vote')
            data.pop('vote')
            data['user_who_created_list_votes'] = Account.objects.get(id=data.get('user_who_created_list_votes'))
            vote_api = ListVotes.objects.create(**data)
            for vote_id in vote_list:
                vote_api.vote.add(Vote.objects.get(id=vote_id))
                vote_api.save()
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class ListVotesApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(ListVotes, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = ListVotesSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(ListVotes, pk=kwargs.get("pk"))
        serializer = ListVotesSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(ListVotes, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
