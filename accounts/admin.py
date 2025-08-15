from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "role",
    ]

    # Customize fieldsets for display in the admin
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "role",
                    "publisher",
                    "subscribed_journalists",
                    "subscribed_publishers",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "role",
                    "publisher",
                    "subscribed_journalists",
                    "subscribed_publishers",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
