# Generated by Django 5.0.1 on 2024-02-26 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_trainernotifications'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainernotifications',
            options={'verbose_name_plural': 'Trainer Notifications'},
        ),
        migrations.CreateModel(
            name='NotifTrainerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainernotifications')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainer')),
            ],
            options={
                'verbose_name_plural': 'Trainer Notification Status',
            },
        ),
    ]
