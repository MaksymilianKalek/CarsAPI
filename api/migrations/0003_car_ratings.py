# Generated by Django 3.2.6 on 2021-08-24 20:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210824_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='ratings',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=[], size=None),
        ),
    ]
