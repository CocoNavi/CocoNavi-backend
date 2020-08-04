from django.urls import path
from . import views

app_name = "pets"

urlpatterns = [
    path("get-pets/", views.get_pets, name="get-pets"),
    path("add-pets/", views.add_pets, name="add-pets"),
]
