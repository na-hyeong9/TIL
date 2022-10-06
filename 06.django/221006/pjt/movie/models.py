from django.db import models

# Create your models here.


class Movie(models.Model):
    # 제목 글자 수 제한
    title = models.CharField(max_length=50)
    # 내용
    summary = models.TextField()
    # 러닝타임
    running_time = models.IntegerField(null=True)
