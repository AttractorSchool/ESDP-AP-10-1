from django.contrib import admin

from webapp.models import Events, Cities, TypeEvents


# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "create_at")
    list_filter = ("id", "description", "create_at")
    search_fields = ("description", "place")
    filter = ("description", "place", "create_at")
    readonly_fields = ("id", "create_at")


class CitiesAdmin(admin.ModelAdmin):
    search_fields = ["citi_name"]
    filter = ["citi_name"]
    readonly_fields = ["id"]


class TypeEventsAdmin(admin.ModelAdmin):
    search_fields = ["events_name"]
    filter = ["events_name"]
    readonly_fields = ["id"]


admin.site.register(Events, EventsAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(TypeEvents, TypeEventsAdmin)
