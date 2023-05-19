from django.contrib import admin

from webapp.models import Events, Cities, TypeEvents, News, Image


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


admin.site.register(Events, EventsAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(TypeEvents, TypeEventsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Image, ImageAdmin)

