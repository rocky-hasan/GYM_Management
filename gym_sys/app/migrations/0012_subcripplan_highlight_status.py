# Generated by Django 5.0.1 on 2024-01-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_subcripplan_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcripplan',
            name='highlight_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]