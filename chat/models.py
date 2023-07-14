import uuid
from django.db import models
from django.utils import timezone
from enum import Enum
import logging

from accounts.models import Account

logger = logging.getLogger(__name__)


class ChatType(Enum):
    PRIVATE = "Private"
    GROUP = "Group"


class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    chat_type = models.CharField(
        max_length=7,
        choices=[(tag.name, tag.value) for tag in ChatType],
        default=ChatType.PRIVATE,
    )
    users = models.ManyToManyField(Account, through='ChatRoomMembership', related_name='chat_rooms')
    avatar = models.ImageField(upload_to='groupchats/', null=True, blank=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='created_groups',
                                null=True, blank=True)

    def is_group_chat(self):
        return self.chat_type == ChatType.GROUP.name

    def get_user_list(self):
        return [user.username for user in self.users.all()]


class ChatRoomMembership(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        logger.debug(f"ChatRoomMembership created: User - {self.user.username}, Room - {self.chat_room.name}")


class File(models.Model):
    file = models.FileField(upload_to='chatfiles/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='files')
    chat_message = models.ForeignKey('ChatMessage', on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='related_files')


class ChatMessage(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)

    def display_timestamp(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        ordering = ['timestamp']
