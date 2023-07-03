from django.urls import path

from webapp.views.events import EventDetailView
from webapp.views.newsline import NewslineView
from webapp.views.profiles import ProfileListView, ProfileDetailView

urlpatterns = [
    path('newsline/', NewslineView.as_view(), name="newsline"),
    path('accounts/', ProfileListView.as_view(), name='account_list'),
    path('accounts/<int:pk>/', ProfileDetailView.as_view(), name='account_detail'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='events_detail')
]
