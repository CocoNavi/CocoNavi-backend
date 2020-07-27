from django.contrib import admin
from . import models

@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    """Pet Admin"""
    list_display = ("__str__", "pet_kinds")

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Pet Photo Admin"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
            return mark_safe(f"<img width=50px src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"
