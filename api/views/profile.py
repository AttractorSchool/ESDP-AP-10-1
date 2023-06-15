from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from api.serializers import AccountSerializer


class AccountsSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = Account.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "Профили отсутствуют"})
        else:
            serializer = AccountSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)