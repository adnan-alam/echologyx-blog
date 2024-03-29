# Generated by Django 3.2.13 on 2022-06-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='example-slug', max_length=160, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='example-title', max_length=125),
            preserve_default=False,
        ),
    ]
