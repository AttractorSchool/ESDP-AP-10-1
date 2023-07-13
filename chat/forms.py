from django import forms
from .models import ChatRoom, Account


class GroupChatForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=Account.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = ChatRoom
        fields = ['name', 'description', 'avatar', 'users']
