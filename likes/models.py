from django.db import models
from core import models as core_models


class Like(core_models.TimeStampedModel):
    #좋아요

    #post에대해 유저가 좋아요를 누르는 행동으로 user와 target이되는 post를 foreign key로 가진다.
    user = models.ForeignKey("users.User",
                             on_delete=models.CASCADE,
                             related_name="likes")
    post = models.ForeignKey("posts.Post",
                             on_delete=models.CASCADE,
                             related_name="likes")

    def __str__(self):
        return f"{self.user} likes {self.post}"