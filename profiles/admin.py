from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from profiles.models import UserNet
from django.utils.translation import gettext_lazy as _


class UserNetAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "middle_name", "email")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            _("info"),
            {
                "fields": (
                    "phone",
                    "avatar",
                    "gender",
                )
            },
        ),
    )


admin.site.register(UserNet, UserNetAdmin)
