from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    content = RichTextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.author}"


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    content = RichTextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.author}"
