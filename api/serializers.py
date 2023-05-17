from rest_framework import serializers

from webapp.models import Events, Cities, TypeEvents


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
    cities = CitiesSerializer(read_only=True)
    type_events = TypeEventsSerializer(read_only=True)

    class Meta:
        model = Events
        fields = ("id", "user", "cities", "type_events", "number_of_seats",
                  "events_at", "user_booked", "user_paid", "description",
                  "start_register_at", "end_register_at", "name",
                  "is_deleted", "place", "price", "create_at", "update_at", "photo")
        read_only = ("id", "create_at", "update_at", "is_deleted")
