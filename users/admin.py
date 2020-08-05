from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "CustomProfile",
            {"fields": ("nickname", "login_method", "uid", "avatar", "point")},
        ),
    )

    list_display = (
        "username",
        "nickname",
        "login_method",
        "uid",
    )

    # def get_thumbnail(self, obj):
    #     return mark_safe(f"<img width=50px src='{obj.avatar.url}' />")

    # get_thumbnail.short_description = "Thumbnail"
