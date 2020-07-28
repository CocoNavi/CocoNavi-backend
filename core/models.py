from django.db import models

class TimeStampedModel(models.Model):
    """Time Stamped Model"""
    #모든 클래스의 부모클래스

    #댓글, post, 등 대부분의 모든것이 생성시간과, 수정시간을 가지기 때문에 만든것이다.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True