# Generated by Django 4.0.1 on 2022-01-22 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 17, 29, 14, 370127)),
        ),
    ]
