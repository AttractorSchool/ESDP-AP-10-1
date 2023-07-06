import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from accounts.models import Account
from api.serializers import SubscriptionLevelSerializer, ChatRequestSerializer, AdminRequestSerializer
from webapp.models import SubscriptionLevel, ChatRequest, AdminRequest, Cities
from django.db.models import Q


class ChatRequestApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            chat_request_list = AdminRequest.objects.filter(chat_request__isnull=False)
            if request.GET.get('order_by'):
                chat_request_list = chat_request_list.order_by(request.GET.get('order_by'))
        except ObjectDoesNotExist:
            response = Response({"error": "Данная операция не доступна"})
            response.status_code = 400
            return response
        else:
            serializer = AdminRequestSerializer(chat_request_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            chat_request_dict = {
                'chat_name': data.pop('chat_name'),
                'description': data.pop('description'),
                'rules': data.pop('rules')
            }
            if 'second_user' in data and data['second_user'] != None:
                chat_request_dict['second_user'] = get_object_or_404(Account, id=data.pop('second_user'))
            else:
                data.pop('second_user')
                chat_request_dict['second_user'] = None
            if 'cities' in data and data['cities'] != None:
                chat_request_dict['cities'] = get_object_or_404(Cities, id=data.pop('cities'))
            else:
                data.pop('cities')
                chat_request_dict['cities'] = None
            serializer = ChatRequestSerializer(data=chat_request_dict)
            if serializer.is_valid():
                chat_request_create = ChatRequest.objects.create(**chat_request_dict)
                data['user_sender'] = get_object_or_404(Account, id=data.pop('user_sender'))
                data['chat_request'] = chat_request_create
                AdminRequest.objects.create(**data)
                return Response({"create": "Запрос успешно создан"})
            else:
                response = Response({'errors': serializer.errors})
                response.status_code = 400
                return response
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class SubscriptionLevelRequestApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            sub_request_list = AdminRequest.objects.filter(sub_level__isnull=False)
        except ObjectDoesNotExist:
            response = Response({"error": "Данная операция не доступна"})
            response.status_code = 400
            return response
        else:
            serializer = AdminRequestSerializer(sub_request_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            data['user_sender'] = Account.objects.get(id=data.pop('user_sender'))
            data['sub_level'] = SubscriptionLevel.objects.get(id=data.pop('sub_level'))
            AdminRequest.objects.create(**data)
            return Response({"create": "Запрос успешно создан"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class SubscriptionLevelApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            level_list = SubscriptionLevel.objects.filter(is_deleted=False)
        except ObjectDoesNotExist:
            response = Response({"error": "Данная операция не доступна"})
            response.status_code = 400
            return response
        else:
            serializer = SubscriptionLevelSerializer(level_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            serializer = SubscriptionLevelSerializer(data=data)
            if serializer.is_valid():
                SubscriptionLevel.objects.create(**data)
                return Response({"create": "Запрос успешно создан"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class SubscriptionLevelDetailApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            sub_level_detail = get_object_or_404(SubscriptionLevel, pk=kwargs.get("pk"))
            serializer = SubscriptionLevelSerializer(sub_level_detail)
        except ObjectDoesNotExist:
            response = Response({"error": "Данная операция не доступна"})
            response.status_code = 400
            return response
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            object = get_object_or_404(SubscriptionLevel, pk=kwargs.get('pk'))
            serializer = SubscriptionLevelSerializer(object, data=data)
            if serializer.is_valid():
                serializer.update(instance=object, validated_data=data)
                return Response(serializer.data)
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(SubscriptionLevel, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})


class RequestApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            request_list = AdminRequest.objects.filter(sub_level__isnull=True, chat_request__isnull=True)
        except ObjectDoesNotExist:
            response = Response({"error": "Данная операция не доступна"})
            response.status_code = 400
            return response
        else:
            serializer = AdminRequestSerializer(request_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            data['user_sender'] = Account.objects.get(id=data.pop('user_sender'))
            AdminRequest.objects.create(**data)
            return Response({"create": "Запрос успешно создан"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class AdminRequestListApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            request_list = AdminRequest.objects.all()
        except ObjectDoesNotExist:
            response = Response({"error": "Данная операция не доступна"})
            response.status_code = 400
            return response
        else:
            serializer = AdminRequestSerializer(request_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class AdminRequestDetailApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            request_detail = get_object_or_404(AdminRequest, pk=kwargs.get("pk"))
            serializer = AdminRequestSerializer(request_detail)
        except ObjectDoesNotExist:
            response = Response({"error": "введите существующий pk"})
            response.status_code = 400
            return response
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            objects = get_object_or_404(AdminRequest, pk=kwargs.get("pk"))
            if 'user_reviewer' in data and data['user_reviewer'] != None:
                data['user_reviewer'] = get_object_or_404(Account, pk=data['user_reviewer'])
            if 'sub_level' in data and data['sub_level'] != None:
                data['sub_level'] = get_object_or_404(SubscriptionLevel, pk=data['sub_level'])
            if 'chat_request' in data and data['chat_request'] != None:
                if 'second_user' in data['chat_request']:
                    data['chat_request']['second_user'] = get_object_or_404(Account,
                                                                            pk=data['chat_request']['second_user'])
                if 'cities' in data['chat_request']:
                    data['chat_request']['cities'] = get_object_or_404(Cities, pk=data['chat_request']['cities'])
                chat_request_object = get_object_or_404(ChatRequest, pk=data['chat_request']['id'])
                chat_serializer = ChatRequestSerializer(chat_request_object, data=data['chat_request'])
                if chat_serializer.is_valid():
                    chat_serializer.update(instance=chat_request_object, validated_data=data.pop('chat_request'))
            request_serializer = AdminRequestSerializer(objects, data=data)
            if request_serializer.is_valid():
                request_serializer.update(instance=objects, validated_data=data)
                return Response(request_serializer.data)
            else:
                response = Response({'errors': request_serializer.errors})
                response.status_code = 400
                return response
        except:
            response = Response({"error": "Данная операция не доступна"})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(AdminRequest, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
