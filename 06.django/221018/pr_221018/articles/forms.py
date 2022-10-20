from django import forms
from .models import Article

# 데이터베이스 기반으로 작성할 것이기 때문에 'forms.ModelForm'을 사용


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image"]
