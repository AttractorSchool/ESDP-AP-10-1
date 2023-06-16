from django.urls import path
from events_app.views.newsline import NewslineView

urlpatterns = [
    path('newsline/', NewslineView.as_view(), name="newsline"),
]
