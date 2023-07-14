from django.contrib import admin

from chat.models import ChatRoom, ChatRoomMembership, ChatMessage, File

admin.site.register(ChatRoom)
admin.site.register(ChatRoomMembership)
admin.site.register(ChatMessage)
admin.site.register(File)
