# Generated by Django 3.2.5 on 2021-08-07 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210808_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newvideo',
            name='username',
        ),
    ]
