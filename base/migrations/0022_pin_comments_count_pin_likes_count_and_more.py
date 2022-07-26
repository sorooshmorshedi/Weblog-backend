# Generated by Django 4.0.1 on 2022-01-23 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_profile_following_alter_comment_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='comments_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pin',
            name='likes_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 9, 54, 51, 95551)),
        ),
    ]
