from ckeditor.fields import RichTextField
from slugify import slugify
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    slug = models.SlugField(max_length=160, unique=True)
    content = RichTextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.slug} | {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, separator="-") + str(uuid.uuid4())
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title, separator="-") + str(uuid.uuid4())

        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    content = RichTextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.post.slug}"


class CustomTemplate(models.Model):
    slug = models.SlugField(
        max_length=160, verbose_name=_("Template Slug"), unique=True
    )
    body_html = RichTextField(verbose_name=_("Body HTML"))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Custom Template")
        verbose_name_plural = _("Custom Templates")

    def __str__(self):
        return f"{self.slug} | Active: {self.is_active}"
