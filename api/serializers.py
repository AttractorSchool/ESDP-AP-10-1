from rest_framework import serializers

from events_app.models import Events, TypeEvents, News, UserBooked
from other_app.models import Cities, Image
from accounts.models import Review, Account


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
    cities = CitiesSerializer()
    type_events = TypeEventsSerializer()
    photo = ImageSerializer()

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
    cities = CitiesSerializer()
    photo = ImageSerializer(many=True)

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
    cities = CitiesSerializer()
    avatar = ImageSerializer()

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
