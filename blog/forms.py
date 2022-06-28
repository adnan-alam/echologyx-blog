from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Post, Comment


User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["post", "content"]
