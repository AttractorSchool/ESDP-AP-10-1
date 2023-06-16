from django.contrib import admin

# Register your models here.

from vote_app.models import Vote, ListVotes, AttachingToBlock, NameVotingTypes, UsersWhoVoted, VotingTypes, \
    VotingOptions


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


admin.site.register(Vote, VoteAdmin)
admin.site.register(ListVotes, ListVotesAdmin)
admin.site.register(AttachingToBlock, AttachingToBlockAdmin)
admin.site.register(NameVotingTypes, NameVotingTypesAdmin)
admin.site.register(UsersWhoVoted, UsersWhoVotedAdmin)
admin.site.register(VotingTypes, VotingTypesAdmin)
admin.site.register(VotingOptions, VotingOptionsAdmin)
