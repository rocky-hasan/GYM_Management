# Generated by Django 5.0.1 on 2024-01-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_assignsubscriber_subscriber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcripplan',
            name='validate_time',
            field=models.IntegerField(null=True),
        ),
    ]
