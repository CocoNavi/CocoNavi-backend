from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models

class User(AbstractUser):
    """Custom User Models"""
    #로그인 방식과 별명, uid, 프로필사진을 가진다.
    LOGIN_GOOGLE = "Google"
    LOGIN_APPLE = "Apple"
    LOGIN_CHOICES = ((LOGIN_GOOGLE, "Google"), (LOGIN_APPLE, "Apple"))
    nickname = models.CharField(max_length=15, unique=True)
    login_method = models.CharField(choices=LOGIN_CHOICES,
                                    max_length=15,
                                    default=LOGIN_GOOGLE)
    uid = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to="users_photos", blank=True, null=True)
    def serializeCustom(self):
        data = {
            "pk": self.pk,
        }
        return data