from django.contrib import admin

from accounts.models import Account, Review


class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "cities")
    list_filter = ("cities", "family_status", "role", "status")
    search_fields = ("last_name", "cities", "email", "created_at")
    filter = ("cities", "family_status", "role", "status")
    readonly_fields = ("id", "created_at", "updated_at")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user_write_review", "user_receive_review", "text")
    list_filter = ("user_write_review", "user_receive_review")
    search_fields = ("user_write_review", "user_receive_review")
    filter = ("user_write_review", "user_receive_review")
    readonly_fields = ("id", "created_at", "updated_at")


admin.site.register(Account, AccountAdmin)
admin.site.register(Review, ReviewAdmin)

