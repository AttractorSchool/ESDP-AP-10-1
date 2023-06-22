from rest_framework import serializers

from accounts.models import Review, Account
from webapp.models import Events, Cities, TypeEvents, News, UserBooked, Image, Vote, NameVotingTypes, VotingTypes, \
    VotingOptions, UsersWhoVoted, ListVotes, AttachingToBlock


class TypeEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEvents
        fields = ("id", "events_name")
        read_only = ("id",)


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ("id", "citi_name")
        read_only = ("id",)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image", "user", "created_at")
        read_only = ("id", "image", "user", "created_at")


class EventsSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(read_only=True)
    type_events = TypeEventsSerializer(read_only=True)

    class Meta:
        model = Events
        fields = (
            "id",
            "name",
            "cities",
            "type_events",
            "events_at",
            "sponsor",
            "number_of_seats",
            "start_register_at",
            "end_register_at",
            "resident_booked",
            "description",
            "place",
            "price",
            "is_deleted",
            "created_at",
            "updated_at",
            "photo",
        )
        read_only = ("id", "created_at", "updated_at", "is_deleted")


class NewsSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(read_only=True)
    photo = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = (
            "id",
            "name",
            "user",
            "cities",
            "description",
            "photo",
            "created_at",
            "updated_at",
            "is_deleted",
        )
        read_only = ("id", "create_at", "update_at", "is_deleted")


class UserBookedSerializer(serializers.ModelSerializer):
    event = EventsSerializer()

    class Meta:
        model = UserBooked
        fields = (
            "id",
            "resident",
            "event",
            "booking_date",
            "date_of_payment",
            "cancellation_date",
        )
        read_only = ("id",)


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "id",
            "user_write_review",
            "user_receive_review",
            "text",
            "like",
            "created_at",
        )
        read_only = ("id",)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "birth_date",
            "about_me",
            "occupation",
            "cities",
            "status",
            "created_at",
            "updated_at",
            "family_status",
            "first_visit_app",
            "likes_qty",
            "avatar",
            "role",
            "email",
            "phone",
            "companies",
            "expertise",
            "resources_available",
            "resources_searching",
            "achievements",
            "goal_for_the_year",
            "request",
            "hobby",
            "education",
            "children",
            "facts_about_me",
            "site",
            "social_links",
        )
        read_only = ("id",)


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = (
            "id",
            "question_to_vote",
            "updated_at",
        )
        read_only = ("id", "updated_at")


class NameVotingTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameVotingTypes
        fields = (
            "id",
            "name_of_voting_type",
        )
        read_only = ("id",)


class VotingTypesSerializer(serializers.ModelSerializer):
    voting_type = NameVotingTypesSerializer(read_only=True)
    vote = VoteSerializer(read_only=True)

    class Meta:
        model = VotingTypes
        fields = (
            "id",
            "voting_type",
            "vote",
            "boolean_value",
        )
        read_only = ("id",)


class VotingOptionsSerializer(serializers.ModelSerializer):
    vote = VoteSerializer(read_only=True)

    class Meta:
        model = VotingOptions
        fields = (
            "id",
            "option",
            "vote",
            "updated_at",
            "is_deleted",
        )
        read_only = ("id", "updated_at")


class UsersWhoVotedSerializer(serializers.ModelSerializer):
    possible_answer = VotingOptionsSerializer(read_only=True)
    users = AccountSerializer(read_only=True)

    class Meta:
        model = UsersWhoVoted
        fields = (
            "id",
            "possible_answer",
            "users",
            "response_at",
        )
        read_only = ("id",)


class ListVotesSerializer(serializers.ModelSerializer):
    user_who_created_list_votes = AccountSerializer(read_only=True)
    vote = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = ListVotes
        fields = (
            "id",
            "name_of_the_vote",
            "user_who_created_list_votes",
            "date_group_was_added_from_polls",
            "updated_at",
            "voting_opening_at",
            "expiration_at",
            "is_deleted",
            "vote",
        )
        read_only = ("id",)


class AttachingToBlockSerializer(serializers.ModelSerializer):
    list_of_votes = ListVotesSerializer(read_only=True)
    events = EventsSerializer(read_only=True)
    news = NewsSerializer(read_only=True)
    users = AccountSerializer(read_only=True)

    class Meta:
        model = AttachingToBlock
        fields = (
            "id",
            "list_of_votes",
            "events",
            "news",
            "users",
            "created_at",
        )
        read_only = ("id",)
