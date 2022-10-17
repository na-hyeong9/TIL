from pickle import TRUE
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

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
    # 이미지
    image = ProcessedImageField(
        upload_to="images/",
        null=True,
        blank=True,
        processors=[ResizeToFill(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
