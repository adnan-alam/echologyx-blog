from django.contrib import admin
from .models import Post, Comment, CustomTemplate


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CustomTemplate)
