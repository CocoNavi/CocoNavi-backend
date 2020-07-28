from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/google/", views.google_login, name="google-login"),
]
