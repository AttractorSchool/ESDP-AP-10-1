from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from accounts.models import Account, FamilyStatus, Role
from api.serializers import AccountSerializer
from webapp.models import Cities, Image


class AccountsSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            accounts = Account.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Профили отсутствуют"})
        else:
            serializer = AccountSerializer(accounts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            data['cities'] = Cities.objects.get(id=data.get('cities'))
            data['family_status'] = FamilyStatus.objects.get(id=data.get('family_status'))
            data['role'] = Role.objects.get(id=data.get('role'))
            data['avatar'] = Image.objects.get(id=data.get('avatar'))
            accounts = Account.objects.create(**data)
            return Response({"create": "Успешно создан"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class AccountApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Account, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = AccountSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(Account, pk=kwargs.get("pk"))
        serializer = AccountSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Account, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delete - {kwargs.get('pk')}": "Мягкое удаление выполнено успешно"})
