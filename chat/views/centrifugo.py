import json
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

from django.views.decorators.http import require_POST

from chat.models import ChatRoom, File, ChatMessage

logger = logging.getLogger(__name__)


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


@csrf_exempt
def publish(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authorized'}, status=403)

    logger.debug(request.body)
    data = json.loads(request.body.decode("utf-8"))
    message = data.get("data", {}).get("message")
    channel = data.get("channel")

    if channel:
        room_uuid_str = channel.split(":")[-1]
        try:
            room_uuid = uuid.UUID(room_uuid_str)
        except ValueError:
            return JsonResponse({'error': 'Invalid UUID'}, status=400)

        try:
            room = ChatRoom.objects.get(id=room_uuid)
        except ChatRoom.DoesNotExist:
            return JsonResponse({'error': 'Room does not exist'}, status=404)

        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            file_instance = File(file=uploaded_file, user=request.user, room=room)
            file_instance.save()
        else:
            file_instance = None

        if message:
            chat_message = ChatMessage(room=room, message=message, user=request.user, file=file_instance)
            chat_message.save()

        response = {
            'result': {
                'message': message,
                'user': request.user.username,
                'avatarUrl': request.user.avatar.image.url if request.user.avatar else None,
                'file': file_instance.file.url if file_instance else None,
            }
        }
        return JsonResponse(response)

    else:
        return JsonResponse({'error': 'Missing data'}, status=400)


@csrf_exempt
@require_POST
def upload_file(request, room_uuid):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authorized'}, status=403)

    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file provided'}, status=400)

    try:
        room = ChatRoom.objects.get(id=room_uuid)
    except ChatRoom.DoesNotExist:
        return JsonResponse({'error': 'Room does not exist'}, status=404)

    uploaded_file = request.FILES['file']
    file_instance = File(file=uploaded_file, user=request.user, room=room)
    file_instance.save()

    return JsonResponse({'file_url': file_instance.file.url})


@csrf_exempt
def subscribe(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authorized'}, status=403)

    logger.debug(request.body)
    response = {
        'result': {}
    }
    return JsonResponse(response)
