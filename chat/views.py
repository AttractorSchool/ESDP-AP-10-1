import json
import uuid
import logging
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from accounts.cookie_auth import CookieJWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from .models import ChatMessage, ChatRoom, ChatType
from .forms import GroupChatForm

logger = logging.getLogger(__name__)
User = get_user_model()


class RoomView(View):
    def get(self, request, room_uuid):
        if not request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)

        room = ChatRoom.objects.filter(id=room_uuid).first()
        if room is None:
            return HttpResponse("Room not found", status=404)

        if room.chat_type == ChatType.PRIVATE.name:
            other_user = room.users.exclude(id=request.user.id).first()
        else:
            other_user = None

        old_messages = ChatMessage.objects.filter(room=room).order_by('timestamp')
        return render(request, 'chat/room.html',
                      {'room_name': room.name, 'room_uuid': str(room.id),
                       'old_messages': old_messages, 'room': room,
                       'other_user': other_user})


class StartChatView(View):
    def get(self, request, email):
        if not request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)

        other_user = get_object_or_404(User, email=email)
        user_rooms = ChatRoom.objects.filter(users=request.user, chat_type=ChatType.PRIVATE.name)
        other_user_rooms = ChatRoom.objects.filter(users=other_user, chat_type=ChatType.PRIVATE.name)
        common_rooms = user_rooms.intersection(other_user_rooms)
        room = common_rooms.first()
        if room is None:
            room = ChatRoom.objects.create(
                name=f'Chat with {other_user.email}',
                chat_type=ChatType.PRIVATE.name
            )
            room.users.add(request.user, other_user)
            room.save()
        return redirect(reverse('room_view', args=[str(room.id)]))


class ChatsView(View):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        authenticator = self.authentication_classes[0]()
        try:
            user_auth_tuple = authenticator.authenticate(request)
        except AuthenticationFailed:
            return HttpResponseRedirect(reverse('login'))
        else:
            if user_auth_tuple:
                request.user, request.auth = user_auth_tuple
            else:
                return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        chatrooms = ChatRoom.objects.filter(users=request.user).distinct()
        chats_with_recipients = []
        default_avatar_url = '/uploads/groupchats/default.png'
        for room in chatrooms:
            chat = ChatMessage.objects.filter(room=room).order_by('-timestamp').first()
            if room.is_group_chat():
                chat_name = room.name
                avatar_url = room.avatar.url if room.avatar else default_avatar_url
                if chat:
                    chats_with_recipients.append({'chat': chat, 'chat_name': chat_name,
                                                  'room_id': str(room.id), 'avatar_url': avatar_url})
                else:
                    chats_with_recipients.append({'chat': None, 'chat_name': chat_name,
                                                  'room_id': str(room.id), 'avatar_url': avatar_url})
            else:
                if chat:
                    recipient = room.users.exclude(id=request.user.id).first()
                    if recipient.first_name and recipient.last_name:
                        chat_name = recipient.first_name + " " + recipient.last_name
                    else:
                        chat_name = recipient.email
                    avatar_url = recipient.avatar.image.url if recipient.avatar else None
                    chats_with_recipients.append({'chat': chat, 'chat_name': chat_name,
                                                  'room_id': str(room.id), 'avatar_url': avatar_url})
        chats_with_recipients.sort(key=lambda x: x['chat'].timestamp if x['chat'] else timezone.now(), reverse=True)
        return render(request, 'chat/chat_list.html', {'chats_with_recipients': chats_with_recipients})


class GroupDetailView(View):
    authentication_classes = [CookieJWTAuthentication, ]
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        authenticator = self.authentication_classes[0]()
        try:
            user_auth_tuple = authenticator.authenticate(request)
        except AuthenticationFailed:
            return HttpResponseRedirect(reverse('login'))
        else:
            if user_auth_tuple:
                request.user, request.auth = user_auth_tuple
            else:
                return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(ChatRoom, pk=kwargs['pk'])
        return render(request, 'chat/group_detail.html', {'group': group})


@csrf_exempt
def connect(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authorized'}, status=403)

    logger.debug(request.body)
    user = request.user.email if request.user.is_authenticated else 'Anonymous'
    response = {
        'result': {
            'user': user
        }
    }
    return JsonResponse(response)


class CreateGroupChatView(View):
    def get(self, request):
        form = GroupChatForm()
        return render(request, 'chat/group_chat.html', {'form': form})

    def post(self, request):
        form = GroupChatForm(request.POST, request.FILES)
        if form.is_valid():
            group_chat = form.save(commit=False)
            group_chat.creator = request.user
            group_chat.chat_type = ChatType.GROUP.name
            group_chat.save()
            form.save_m2m()
            return redirect(reverse('room_view', args=[str(group_chat.id)]))
        return render(request, 'chat/create_group_chat.html', {'form': form})


@csrf_exempt
def publish(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authorized'}, status=403)

    logger.debug(request.body)
    data = json.loads(request.body.decode("utf-8"))
    message = data.get("data", {}).get("message")
    channel = data.get("channel")
    if channel and message:
        room_uuid_str = channel.split(":")[-1]
        try:
            room_uuid = uuid.UUID(room_uuid_str)
        except ValueError:
            return JsonResponse({'error': 'Invalid UUID'}, status=400)

        try:
            room = ChatRoom.objects.get(id=room_uuid)
        except ChatRoom.DoesNotExist:
            return JsonResponse({'error': 'Room does not exist'}, status=404)

        chat_message = ChatMessage(room=room, message=message, user=request.user)
        chat_message.save()

    response = {
        'result': {
            'message': message,
            'user': request.user.username
        }
    }
    return JsonResponse(response)


@csrf_exempt
def subscribe(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authorized'}, status=403)

    logger.debug(request.body)
    response = {
        'result': {}
    }
    return JsonResponse(response)
