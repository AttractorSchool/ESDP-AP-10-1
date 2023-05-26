from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "cities")
    list_filter = ("cities", "family_status", "role", "status")
    search_fields = ("last_name", "cities", "email", "created_at")
    filter = ("cities", "family_status", "role", "status")
    readonly_fields = ("id", "created_at", "updated_at")


admin.site.register(Account, AccountAdmin)
