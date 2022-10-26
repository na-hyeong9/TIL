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
    # 메서드를 마치 필드인 것 처럼 사용 가능
    # 참고 https://hwan-hobby.tistory.com/148
    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"
