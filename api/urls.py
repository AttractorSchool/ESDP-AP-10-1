from django.urls import path

from api.views.events_api_view import EventsSimpleView, EventApiView
from api.views.news_api_view import NewsSimpleView, NewsApiView
from api.views.profile import AccountsSimpleView
from api.views.reviews_api_view import ReviewsSimpleView
from api.views.newsline import NewslineApiView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list"),
    path('events/<int:pk>', EventApiView.as_view(), name="events"),
    path('news/', NewsSimpleView.as_view(), name="news_list"),
    path('news/<int:pk>', NewsApiView.as_view(), name="news"),
    path("reviews/", ReviewsSimpleView.as_view(), name="reviews_list_api"),
    path("newsline/", NewslineApiView.as_view(), name="newsline_api"),
    path("accounts/", AccountsSimpleView.as_view(), name="accounts_api"),

]
