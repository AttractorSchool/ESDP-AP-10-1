from django.urls import path

from api.views.events_api_view import EventsSimpleView, EventApiView, EventCreateApiView
from api.views.news_api_view import NewsSimpleView
from api.views.reviews_api_view import ReviewsSimpleView
from api.views.newsline import NewslineApiView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list"),
    path('events/<int:pk>', EventApiView.as_view(), name="events"),
    path('events/create', EventCreateApiView.as_view(), name="events_create"),
    path('news/', NewsSimpleView.as_view(), name="news_list"),
    path("reviews/", ReviewsSimpleView.as_view(), name="reviews_list_api"),
    path("newsline/", NewslineApiView.as_view(), name="newsline_api"),
]
