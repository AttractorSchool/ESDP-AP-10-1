from django.urls import path

from api.views.attaching_to_block_api_view import AttachingToBlockSimpleView, AttachingToBlockApiView
from api.views.events_api_view import EventsSimpleView, EventApiView
from api.views.list_votes import ListVotesSimpleView, ListVotesApiView
from api.views.name_voting_types_api_view import NameVotingTypesSSimpleView, NameVotingTypesSApiView
from api.views.news_api_view import NewsSimpleView, NewsApiView
from api.views.profile import AccountsSimpleView
from api.views.reviews_api_view import ReviewsSimpleView
from api.views.newsline import NewslineApiView
from api.views.users_who_voted_api_view import UsersWhoVotedSimpleView, UsersWhoVotedApiView
from api.views.vote_api_view import VoteApiView, VoteSimpleView
from api.views.voting_options import VotingOptionsSimpleView, VotingOptionsApiView
from api.views.voting_types_api_view import VotingTypesSimpleView, VotingTypesApiView

urlpatterns = [
    path('events/', EventsSimpleView.as_view(), name="events_list"),
    path('events/<int:pk>', EventApiView.as_view(), name="events"),
    path('news/', NewsSimpleView.as_view(), name="news_list"),
    path('news/<int:pk>', NewsApiView.as_view(), name="news"),
    path('vote/', VoteSimpleView.as_view(), name="vote_list"),
    path('vote/<int:pk>', VoteApiView.as_view(), name="vote"),
    path('name_voting_types/', NameVotingTypesSSimpleView.as_view(), name="name_voting_types_list"),
    path('name_voting_types/<int:pk>', NameVotingTypesSApiView.as_view(), name="name_voting_types"),
    path('voting_types/', VotingTypesSimpleView.as_view(), name="voting_types_list"),
    path('voting_types/<int:pk>', VotingTypesApiView.as_view(), name="voting_types"),
    path('voting_options/', VotingOptionsSimpleView.as_view(), name="voting_options_list"),
    path('voting_options/<int:pk>', VotingOptionsApiView.as_view(), name="voting_options"),
    path('users_who_voted/', UsersWhoVotedSimpleView.as_view(), name="users_who_voted_list"),
    path('users_who_voted/<int:pk>', UsersWhoVotedApiView.as_view(), name="users_who_voted"),
    path('list_of_votes/', ListVotesSimpleView.as_view(), name="list_of_votes_list"),
    path('list_of_votes/<int:pk>', ListVotesApiView.as_view(), name="list_of_votes"),
    path('attaching_to_block/', AttachingToBlockSimpleView.as_view(), name="attaching_to_block_list"),
    path('attaching_to_block/<int:pk>', AttachingToBlockApiView.as_view(), name="attaching_to_block"),
    path("reviews/", ReviewsSimpleView.as_view(), name="reviews_list_api"),
    path("newsline/", NewslineApiView.as_view(), name="newsline_api"),
    path("accounts/", AccountsSimpleView.as_view(), name="accounts_api"),
]
