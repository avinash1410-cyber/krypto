# Generated by Django 4.0 on 2022-06-27 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0002_remove_alert_user_customer_alert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='alert',
        ),
        migrations.AddField(
            model_name='alert',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alert.customer'),
        ),
    ]
