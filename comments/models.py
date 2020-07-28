from django.db import models
from core import models as core_models


class Comment(core_models.TimeStampedModel):
    #댓글

    #댓글 내용을 가지고, 댓글을 쓴 유저와, Target이 되는 post를 foreign key로 가진다.
    text = models.TextField(max_length=100)
    user = models.ForeignKey("users.User",
                             on_delete=models.CASCADE,
                             related_name="comments")
    post = models.ForeignKey("posts.Post",
                             on_delete=models.CASCADE,
                             related_name="comments")

    def __str__(self):
        return f"{self.user} comments to {self.post}"

    def comment_likes_count(self):
        return self.commentLikes.count()
    comment_likes_count.short_description = "comment_likes"

    def serializeCustom(self):
        data = {
            "pk": self.pk,
            "text": self.text,
            "host": self.user.pk,
            "host_name": self.user.nickname,
            "likes_number": self.comment_likes_count(),
            "created":str(self.created),
            "updated":str(self.updated),
            "is_deleted":self.is_deleted
        }
        return data