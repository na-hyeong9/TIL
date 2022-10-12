from django.db import models

# django에서 제공하는 회원가입 모델 적용하기 >> 클래스 상속
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
