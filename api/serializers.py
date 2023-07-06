from rest_framework import serializers

from accounts.models import Review, Account, FamilyStatus, Role, Status
from webapp.models import Events, Cities, TypeEvents, News, UserBooked, Image, Vote, NameVotingTypes, VotingTypes, \
    VotingOptions, UsersWhoVoted, ListVotes, AttachingToBlock, SubscriptionLevel, ChatRequest, AdminRequest


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


class FamilyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyStatus
        fields = ("id", "name")
        read_only = ("id",)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "name")
        read_only = ("id",)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("id", "name")
        read_only = ("id",)


class AccountSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

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


class SubscriptionLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionLevel
        fields = (
            "id",
            "level_name",
            "price",
            "created_at",
            "updated_at",
            "is_deleted"
        )
        read_only = ("id", "created_at", "updated_at")

    def validate_level_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Имя уровня подписки не может иметь менее 3 символов")
        return value

    def validate_price(self, value):
        value = int(value)
        if value < 1000:
            raise serializers.ValidationError("Цена подписки должна быть больше 1000 ед.")
        return value


class ChatRequestSerializer(serializers.ModelSerializer):
    second_user = AccountSerializer(read_only=True)
    cities = CitiesSerializer(read_only=True)

    class Meta:
        model = ChatRequest
        fields = (
            "id",
            "chat_name",
            "second_user",
            "cities",
            "description",
            "rules"
        )
        read_only = ("id",)

    def validate_chat_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Нужно название чата имеющее 3 и более символов")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Нужно написать краткое описание чата (больше 10 символов)")
        return value

    def validate_rules(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Нужны минимальные правила")
        return value


class AdminRequestSerializer(serializers.ModelSerializer):
    user_reviewer = AccountSerializer(read_only=True)
    user_sender = AccountSerializer(read_only=True)
    sub_level = SubscriptionLevelSerializer(read_only=True)
    chat_request = ChatRequestSerializer(read_only=True)

    class Meta:
        model = AdminRequest
        fields = (
            "id",
            "user_reviewer",
            "user_sender",
            "created_at",
            "closed_at",
            "approved",
            "request_text",
            "response_text",
            "sub_level",
            "chat_request",
            "is_deleted"
        )
        read_only = ("id", "created_at")

    def validate_request_text(self, value):
        if len(value) < 3 or len(value) == 0:
            raise serializers.ValidationError("Текст запроса должен иметь 3 и более символов или быть пустым")
        return value

    def validate_response_text(self, value):
        if len(value) < 3 or len(value) == 0:
            raise serializers.ValidationError("Текст ответа на запрос должен иметь 3 и более символов или быть пустым")
        return value
