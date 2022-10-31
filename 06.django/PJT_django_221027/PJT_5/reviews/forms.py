from django import forms
from .models import Review, Comment


class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
