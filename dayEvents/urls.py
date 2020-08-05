from django.urls import path
from . import views

app_name = "dayEvents"

urlpatterns = [
    path("add-events/", views.add_events, name="add-events"),
    path("revise-events/", views.revise_events, name="revise-events"),
    path("get-events-date/", views.get_events_date, name="get-events-date"),
    path("get-events-month/", views.get_events_month, name="get-events-month"),
]
