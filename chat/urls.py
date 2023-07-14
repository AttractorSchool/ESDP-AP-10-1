from django.urls import path

from chat.views import StartChatView, RoomView, ChatsView, CreateGroupChatView, GroupDetailView, UpdateGroupChatView, \
    connect, subscribe, publish, upload_file

urlpatterns = [
    path('start_chat/<str:email>/', StartChatView.as_view(), name='start_chat'),
    path('<uuid:room_uuid>/', RoomView.as_view(), name='room_view'),
    path('all/', ChatsView.as_view(), name='chat_list'),
    path('start_group_chat/', CreateGroupChatView.as_view(), name='group_chat'),
    path('group/<uuid:pk>/', GroupDetailView.as_view(), name='group_detail'),
    path('group/update/<uuid:room_uuid>', UpdateGroupChatView.as_view(), name='update_chat'),
    path('chatfiles/<uuid:room_uuid>/', upload_file, name='upload_file'),
    path('centrifugo/connect/', connect, name='connect'),
    path('centrifugo/subscribe/', subscribe, name='subscribe'),
    path('centrifugo/publish/', publish, name='publish'),
]
