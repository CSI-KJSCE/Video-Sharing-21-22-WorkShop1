# Generated by Django 3.2.5 on 2021-08-07 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_newvideo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newvideo',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='newvideo',
            name='video',
            field=models.FileField(default=None, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
