from django.urls import path

from api.views.events_api_view import EventsSimpleView, EventApiView
from api.views.news_api_view import NewsSimpleView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list"),
    path('events/<int:pk>', EventApiView.as_view(), name="events_create"),
    path('news/', NewsSimpleView.as_view(), name="news_list"),
]
