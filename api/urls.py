from django.urls import path

from api.views.events_api_view import EventsSimpleView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list"),
]
