from rest_framework import serializers

from webapp.models import Events, Cities, TypeEvents, News, UserBooked


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


class EventsSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer()
    type_events = TypeEventsSerializer()

    class Meta:
        model = Events
        fields = ("id", "name", "cities", "type_events", "events_at",
                  "sponsor", "number_of_seats", "start_register_at", "end_register_at",
                  "resident_booked", "description", "place", "price",
                  "is_deleted", "created_at", "updated_at", "photo")
        read_only = ("id", "created_at", "updated_at", "is_deleted")


class NewsSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(read_only=True)

    class Meta:
        model = News
        fields = (
            "id", "name", "user", "cities", "description",
            "photo", "created_at", "updated_at", "is_deleted"
        )
        read_only = ("id", "create_at", "update_at", "is_deleted")


class UserBookedSerializer(serializers.ModelSerializer):
    event = EventsSerializer()

    class Meta:
        model = UserBooked
        fields = ("id", "resident", "event", "booking_date", "date_of_payment", "cancellation_date",)
        read_only = ("id",)
