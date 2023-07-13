from django.urls import path
from . import views
from .views import StartChatView, RoomView, ChatsView, CreateGroupChatView

urlpatterns = [
    path('start_chat/<str:email>/', StartChatView.as_view(), name='start_chat'),
    path('<uuid:room_uuid>/', RoomView.as_view(), name='room_view'),
    path('all/', ChatsView.as_view(), name='chat_list'),
    path('start_group_chat/', CreateGroupChatView.as_view(), name='group_chat'),
    path('centrifugo/connect/', views.connect, name='connect'),
    path('centrifugo/subscribe/', views.subscribe, name='subscribe'),
    path('centrifugo/publish/', views.publish, name='publish'),
]