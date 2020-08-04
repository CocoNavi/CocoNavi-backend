from django.urls import path
from . import views

app_name = "dayEvents"

urlpatterns = [
    path("add-events/", views.add_events, name="add-events"),
]
