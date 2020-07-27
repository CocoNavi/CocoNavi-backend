from django.db import models
from core import models as core_models
from users import models as user_models

class DayEvent(core_models.TimeStampedModel):
    pet = models.ForeignKey("pets.Pet", related_name="dayEvents", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()
    date = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.nickname}'s {self.title} at {self.date}"