from django.db import models
from core import models as core_models
from users import models as user_models

class DayEvent(core_models.TimeStampedModel):
    #캘린더에 사용되는 event

    #필드로 제목, 내용, 날짜를 가지고 이 일정을 가지는 pet을 foreignkey로 가진다.
    pet = models.ForeignKey("pets.Pet", related_name="dayEvents", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()
    date = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.nickname}'s {self.title} at {self.date}"