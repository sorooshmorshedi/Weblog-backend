# Generated by Django 4.0.1 on 2022-02-01 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0057_remove_account_email_remove_account_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 11, 23, 53, 359149)),
        ),
    ]
