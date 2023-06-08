from django.urls import path

from api.views.events_api_view import EventsSimpleView, EventsDetailSimpleView, EventsDeleteSimpleView, \
    EventsUpdateView, EventsCreateView
from api.views.news_api_view import NewsSimpleView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list"),
    path('events/create', EventsCreateView.as_view(), name="events_create"),
    path('events/detail/<int:pk>', EventsDetailSimpleView.as_view(), name="events_detail"),
    path('events/update/<int:pk>', EventsUpdateView.as_view(), name="events_update"),
    path('events/delete/<int:pk>', EventsDeleteSimpleView.as_view(), name="events_delete"),
    path('news/', NewsSimpleView.as_view(), name="news_list"),
]
