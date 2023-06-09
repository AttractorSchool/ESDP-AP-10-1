from django.contrib import admin

from webapp.models import Events, Cities, TypeEvents, News, Image, UserBooked


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


admin.site.register(Events, EventsAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(TypeEvents, TypeEventsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(UserBooked, UserBookedAdmin)
