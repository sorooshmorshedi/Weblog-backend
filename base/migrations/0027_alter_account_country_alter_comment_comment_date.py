# Generated by Django 4.0.1 on 2022-01-24 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_pin_user_name_alter_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 14, 43, 13, 116387)),
        ),
    ]
