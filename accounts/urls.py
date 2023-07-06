from django.urls import path
from accounts.views.auth import RegisterUserView, LoginUserView, LogoutUserView
from accounts.views.profile import ProfileView, ProfileListView


urlpatterns = [
    path('profile-list/', ProfileListView.as_view(), name="profile_list"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='auth_logout'),
]
