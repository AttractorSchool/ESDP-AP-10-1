from django.urls import path
from . import views
from .views import StartChatView, RoomView, ChatsView

urlpatterns = [
    path('start_chat/<str:email>/', views.StartChatView.as_view(), name='start_chat'),
    path('<uuid:room_uuid>/', RoomView.as_view(), name='room_view'),
    path('all/', ChatsView.as_view(), name='chat_list'),
    path('centrifugo/connect/', views.connect, name='connect'),
    path('centrifugo/subscribe/', views.subscribe, name='subscribe'),
    path('centrifugo/publish/', views.publish, name='publish'),
]