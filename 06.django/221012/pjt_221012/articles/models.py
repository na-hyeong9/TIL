from pickle import TRUE
from django.db import models

# Create your models here.


class Article(models.Model):
    # 제목 글자 수 제한
    title = models.CharField(max_length=20)
    # 내용
    content = models.TextField()
    # 작성 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated_at = models.DateTimeField(auto_now=True)
