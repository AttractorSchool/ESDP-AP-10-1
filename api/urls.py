from django.urls import path

from api.views.events_api_view import EventsSimpleView
from api.views.news_api_view import NewsSimpleView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list"),
    path('news/', NewsSimpleView.as_view(), name="news_list"),
]
