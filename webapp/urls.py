from django.urls import path
from webapp.views.events import EventDetailView
from webapp.views.news import NewsCreateView, NewsDetail, NewsUpdateView, NewsDeleteView
from webapp.views.index import index
from webapp.views.newsline import NewslineView
from webapp.views.profile import ProfileListView, ProfileDetailView

urlpatterns = [
    path('', index, name='index'),
    path('newsline/', NewslineView.as_view(), name="newsline"),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('news/update/<int:pk>/', NewsUpdateView.as_view(), name='news_update'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/confirm_delete/<int:pk>/', NewsDeleteView.as_view(), name='news_confirm_delete'),
    path('accounts/', ProfileListView.as_view(), name='account_list'),
    path('accounts/<int:pk>/', ProfileDetailView.as_view(), name='account_detail'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='events_detail')
]
