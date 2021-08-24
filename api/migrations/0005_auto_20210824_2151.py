# Generated by Django 3.2.6 on 2021-08-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_car_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='avg_rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='rates_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
