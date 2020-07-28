from django.db import models
from core import models as core_models


class Board(core_models.TimeStampedModel):
    """Custom Board"""
    #게시판
    title = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return f"{self.title}"
