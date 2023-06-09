from django.urls import path

from accounts.profile import ProfileView

urlpatterns = [
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
]
