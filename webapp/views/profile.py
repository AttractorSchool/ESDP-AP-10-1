from django.views.generic import ListView, DetailView

from accounts.models import Account


class ProfileListView(ListView):
    model = Account
    template_name = 'profile_list_django.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_account = Account.objects.filter(username=self.request.user.username).first()
        context['user_account'] = user_account
        return context


class ProfileDetailView(DetailView):
    model = Account
    template_name = 'profile_detail.html'
    context_object_name = 'account'
