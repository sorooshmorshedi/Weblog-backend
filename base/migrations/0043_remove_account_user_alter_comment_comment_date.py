# Generated by Django 4.0.1 on 2022-01-26 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_alter_account_token_alter_comment_comment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 0, 43, 49, 755497)),
        ),
    ]
