from django.contrib import admin

from webapp.models import Events, Cities, TypeEvents, News, Image, UserBooked, Vote, ListVotes, AttachingToBlock, \
    NameVotingTypes, UsersWhoVoted, VotingTypes, VotingOptions, SubscriptionLevel, AdminRequest, ChatRequest


# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "created_at")
    list_filter = ("id", "description", "created_at")
    search_fields = ("description", "place")
    filter = ("description", "place", "created_at")
    readonly_fields = ("id", "created_at")


class CitiesAdmin(admin.ModelAdmin):
    search_fields = ["citi_name"]
    filter = ["citi_name"]
    readonly_fields = ["id"]


class TypeEventsAdmin(admin.ModelAdmin):
    search_fields = ["events_name"]
    filter = ["events_name"]
    readonly_fields = ["id"]


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cities", "user", "description", "created_at")
    list_filter = ("id", "name", "cities", "user", "created_at")
    search_fields = ("name", "cities", "user", "created_at")
    filter = ("name", "user", "cities", "created_at")
    readonly_fields = ("id", "created_at")


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_filter = ("id", "user", "created_at")
    search_fields = ("user", "created_at")
    filter = ("user", "created_at")
    readonly_fields = ("id", "created_at")


class UserBookedAdmin(admin.ModelAdmin):
    list_display = ("id", "resident", "event", "booking_date", "date_of_payment", "cancellation_date")
    list_filter = ("id", "resident", "event", "booking_date", "date_of_payment", "cancellation_date")
    search_fields = ("resident", "event", "booking_date", "date_of_payment", "cancellation_date")
    filter = ("resident", "event", "booking_date", "date_of_payment", "cancellation_date")
    readonly_fields = ("id",)


class VoteAdmin(admin.ModelAdmin):
    list_display = ("id", "question_to_vote", "updated_at")
    list_filter = ("id", "question_to_vote", "updated_at")
    search_fields = ("question_to_vote", "updated_at")
    filter = ("updated_at", "question_to_vote")
    readonly_fields = ("id", "updated_at")


class ListVotesAdmin(admin.ModelAdmin):
    list_display = ("id", "name_of_the_vote", "updated_at")
    list_filter = ("id", "name_of_the_vote", "updated_at")
    search_fields = ("name_of_the_vote", "updated_at")
    filter = ("name_of_the_vote", "updated_at")
    readonly_fields = ("id", "updated_at")


class AttachingToBlockAdmin(admin.ModelAdmin):
    list_display = ("id", "list_of_votes", "created_at")
    list_filter = ("id", "list_of_votes", "created_at")
    search_fields = ("list_of_votes", "place")
    filter = ("list_of_votes", "created_at")
    readonly_fields = ("id", "created_at")


class NameVotingTypesAdmin(admin.ModelAdmin):
    list_display = ("id", "name_of_voting_type")
    list_filter = ("id", "name_of_voting_type")
    search_fields = ("name_of_voting_type",)
    filter = ("name_of_voting_type",)
    readonly_fields = ("id", "name_of_voting_type")


class UsersWhoVotedAdmin(admin.ModelAdmin):
    list_display = ("id", "users", "response_at")
    list_filter = ("id", "users", "response_at")
    search_fields = ("users", "response_at")
    filter = ("users", "response_at")
    readonly_fields = ("id", "response_at")


class VotingTypesAdmin(admin.ModelAdmin):
    list_display = ("id", "voting_type", "boolean_value")
    list_filter = ("id", "voting_type", "boolean_value")
    search_fields = ("voting_type", "boolean_value")
    filter = ("voting_type", "boolean_value")
    readonly_fields = ("id", "boolean_value")


class VotingOptionsAdmin(admin.ModelAdmin):
    list_display = ("id", "vote", "updated_at")
    list_filter = ("id", "vote", "updated_at")
    search_fields = ("vote", "updated_at")
    filter = ("vote", "updated_at")
    readonly_fields = ("id", "updated_at")


class SubscriptionLevelAdmin(admin.ModelAdmin):
    list_display = ("id", "level_name", "price", "created_at", "updated_at", "is_deleted")
    list_filter = ("id", "level_name", "price", "created_at", "updated_at", "is_deleted")
    search_fields = ("level_name", "price", "is_deleted")
    filter = ("level_name", "price", "created_at", "updated_at", "is_deleted")
    readonly_fields = ("id", "created_at", "updated_at")


class ChatRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "chat_name", "second_user", "cities", "description", "rules")
    list_filter = ("id", "chat_name", "second_user", "cities", "description", "rules")
    search_fields = ("chat_name", "second_user", "cities", "description", "rules")
    filter = ("chat_name", "second_user", "cities", "description", "rules")
    readonly_fields = ("id",)


class AdminRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user_reviewer", "user_sender", "created_at", "closed_at", "approved", "request_text", "response_text",
        "sub_level", "chat_request", "is_deleted")
    list_filter = (
        "id", "user_reviewer", "user_sender", "created_at", "closed_at", "approved", "request_text", "response_text",
        "sub_level", "chat_request", "is_deleted")
    search_fields = (
        "user_reviewer", "user_sender", "approved", "request_text", "response_text", "sub_level", "chat_request", "is_deleted")
    filter = (
        "id", "user_reviewer", "user_sender", "created_at", "closed_at", "approved", "request_text", "response_text",
        "sub_level", "chat_request", "is_deleted")
    readonly_fields = ("id", "created_at")


admin.site.register(Events, EventsAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(TypeEvents, TypeEventsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(UserBooked, UserBookedAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(ListVotes, ListVotesAdmin)
admin.site.register(AttachingToBlock, AttachingToBlockAdmin)
admin.site.register(NameVotingTypes, NameVotingTypesAdmin)
admin.site.register(UsersWhoVoted, UsersWhoVotedAdmin)
admin.site.register(VotingTypes, VotingTypesAdmin)
admin.site.register(VotingOptions, VotingOptionsAdmin)
admin.site.register(SubscriptionLevel, SubscriptionLevelAdmin)
admin.site.register(ChatRequest, ChatRequestAdmin)
admin.site.register(AdminRequest, AdminRequestAdmin)
