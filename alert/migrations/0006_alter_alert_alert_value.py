# Generated by Django 4.0 on 2022-06-29 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0005_alert_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
