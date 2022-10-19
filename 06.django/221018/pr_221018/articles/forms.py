from django.db import models
from .models import Article
from django.forms import ModelForm

# 데이터베이스 기반으로 작성할 것이기 때문에 'forms.ModelForm'을 사용


class ArticleForm(models, ModelForm):
    class Mata:
        model = Article
        fields = ["title", "content", "image"]
