# Generated by Django 5.0.7 on 2024-10-06 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_todotask_description_alter_todotask_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='created',
            field=models.DateField(default=datetime.datetime(2024, 10, 6, 14, 16, 34, 4404, tzinfo=datetime.timezone.utc)),
        ),
    ]
