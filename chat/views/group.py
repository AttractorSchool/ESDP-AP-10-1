from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

from accounts.cookie_auth import CookieJWTAuthentication
from chat.forms import GroupChatForm
from chat.models import ChatRoom, ChatType


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
        return render(request, 'chat/group_detail.html', {'group': group, 'current_user': request.user})


class CreateGroupChatView(View):
    def get(self, request):
        form = GroupChatForm(user=request.user)
        return render(request, 'chat/group_chat.html', {'form': form})

    def post(self, request):
        form = GroupChatForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            group_chat = form.save(commit=False)
            group_chat.creator = request.user
            group_chat.chat_type = ChatType.GROUP.name
            group_chat.save()
            form.save_m2m()
            group_chat.users.add(request.user)
            return redirect(reverse('room_view', args=[str(group_chat.id)]))
        return render(request, 'chat/create_group_chat.html', {'form': form})


class UpdateGroupChatView(View):
    def get(self, request, room_uuid):
        group_chat = get_object_or_404(ChatRoom, pk=room_uuid)
        if request.user != group_chat.creator:
            return HttpResponse('Unauthorized', status=401)
        form = GroupChatForm(instance=group_chat, user=request.user)
        return render(request, 'chat/update_group_chat.html', {'form': form, 'group_chat': group_chat})

    def post(self, request, room_uuid):
        group_chat = get_object_or_404(ChatRoom, pk=room_uuid)
        if request.user != group_chat.creator:
            return HttpResponse('Unauthorized', status=401)
        form = GroupChatForm(request.POST, request.FILES, instance=group_chat, user=request.user)
        if form.is_valid():
            updated_group_chat = form.save()
            updated_group_chat.users.add(request.user)
            return redirect(reverse('room_view', args=[str(updated_group_chat.id)]))
        return render(request, 'chat/update_group_chat.html', {'form': form, 'group_chat': group_chat})
