# Generated by Django 4.0 on 2022-06-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0004_alter_alert_user_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='coin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
