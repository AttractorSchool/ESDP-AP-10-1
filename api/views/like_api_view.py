from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import Account


class UserLikeView(APIView):
    def post(self, request, id, *args, **kwargs):
        try:
            page_owner = get_object_or_404(Account, pk=id)
            print(page_owner)
            page_owner.likes_qty += 1
            page_owner.save()
            return JsonResponse({"likes_qty": page_owner.likes_qty}, status=200)
        except Account.DoesNotExist:
            response = Response({'error': "Пользователь не найден"})
            response.status_code = 404
            return response
        except Exception as e:
            response = Response({'error': "Ошибка"})
            response.status_code = 400
            return response
