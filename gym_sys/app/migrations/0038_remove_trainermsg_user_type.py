# Generated by Django 5.0.1 on 2024-02-26 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_trainermsg_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainermsg',
            name='user_type',
        ),
    ]