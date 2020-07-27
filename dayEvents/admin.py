from django.contrib import admin
from . import models

@admin.register(models.DayEvent)
class DayEventsAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
