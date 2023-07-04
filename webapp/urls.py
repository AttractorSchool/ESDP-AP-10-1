from django.urls import path
from webapp.views.newsline import NewslineView

urlpatterns = [
    path('newsline/', NewslineView.as_view(), name="newsline"),
]
