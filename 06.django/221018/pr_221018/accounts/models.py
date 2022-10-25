from django.db import models
from django.conf import settings

# django 내장 모듈 사용
# contrib (contributed) :  기여하다
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="followings"
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"
