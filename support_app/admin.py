from django.contrib import admin
from other_app.models import Cities, Image

# Register your models here.


class CitiesAdmin(admin.ModelAdmin):
    search_fields = ["citi_name"]
    filter = ["citi_name"]
    readonly_fields = ["id"]


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_filter = ("id", "user", "created_at")
    search_fields = ("user", "created_at")
    filter = ("user", "created_at")
    readonly_fields = ("id", "created_at")


admin.site.register(Cities, CitiesAdmin)
admin.site.register(Image, ImageAdmin)
