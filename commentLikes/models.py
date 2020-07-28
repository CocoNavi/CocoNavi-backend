from django.db import models
from core import models as core_models


class CommentLike(core_models.TimeStampedModel):
    #댓글좋아요

    #좋아요를 누른 유저와 Target이 되는 댓글을 Foreignkey로 가진다
    user = models.ForeignKey("users.User",
                             on_delete=models.CASCADE,
                             related_name="commentLikes")
    comment = models.ForeignKey("comments.Comment",
                             on_delete=models.CASCADE,
                             related_name="commentLikes")

    def __str__(self):
        return f"{self.user} likes {self.comment}"

