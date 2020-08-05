from django.db import models
from core import models as core_models
from users import models as user_models


class DayEvent(core_models.TimeStampedModel):
    # 캘린더에 사용되는 event

    # 필드로 제목, 내용, 날짜를 가지고 이 일정을 가지는 pet을 foreignkey로 가진다.
    pet = models.ForeignKey(
        "pets.Pet", related_name="dayEvents", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "users.User", related_name="dayEvents", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=20)
    text = models.TextField()
    year = models.CharField(max_length=4, default=1)
    month = models.CharField(max_length=2, default=1)
    date = models.CharField(max_length=2, default=1)

    def __str__(self):
        return f"{self.pet} {self.title} at {self.year}-{self.month}-{self.date}"

    def serialize_custom(self):
        data = {
            "pk": f"{self.pk}",
            "pet_name": self.pet.name,
            "title": self.title,
            "text": self.text,
            "date": f"{self.year}-{self.month}-{self.date}",
        }
        return data

    def serialize_custom1(self):
        data = {
            "pk": f"{self.pk}",
            "pet_name": self.pet.name,
            "year": self.year,
            "month": self.month,
            "day": self.date,
            "title": self.title,
        }
        return data
