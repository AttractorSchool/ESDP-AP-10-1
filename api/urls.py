from django.urls import path

from api.views.events_api_view import EventsSimpleView, EventApiView, EventCreateApiView
from api.views.news_api_view import NewsSimpleView
from api.views.reviews_api_view import ReviewsSimpleView
from api.views.newsline import NewslineApiView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list_api"),
    path('events/<int:pk>', EventApiView.as_view(), name="event_detail_api"),
    path('events/create', EventCreateApiView.as_view(), name="event_create_api"),
    path('news/', NewsSimpleView.as_view(), name="news_list_api"),
    path("reviews/", ReviewsSimpleView.as_view(), name="reviews_list_api"),
    path("newsline/", NewslineApiView.as_view(), name="newsline_api"),
]
