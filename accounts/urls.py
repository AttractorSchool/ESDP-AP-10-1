from django.urls import path

from accounts.views.profile import ProfileView, ProfileListView

urlpatterns = [
    path('profile-list/', ProfileListView.as_view(), name="profile_list"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
]
