from django import forms
from .models import ChatRoom, Account


class GroupChatForm(forms.ModelForm):
    class UserChoiceField(forms.ModelMultipleChoiceField):
        def label_from_instance(self, obj):
            return obj.get_full_name() or obj.email

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['users'].queryset = Account.objects.exclude(id=user.id)

    users = UserChoiceField(
        queryset=Account.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = ChatRoom
        fields = ['name', 'description', 'avatar', 'users']

