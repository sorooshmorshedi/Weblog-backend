# Generated by Django 4.0.1 on 2022-01-24 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_comment_comment_date_alter_like_like_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 9, 37, 49, 490080)),
        ),
    ]
