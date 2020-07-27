from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "host", "board", "count_comments",
                    "count_likes", "created", "updated")

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Post Photo Admin"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
            return mark_safe(f"<img width=50px src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"