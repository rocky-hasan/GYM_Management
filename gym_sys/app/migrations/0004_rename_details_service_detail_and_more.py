# Generated by Django 5.0.1 on 2024-01-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_banners'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='details',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='full_name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(default=2, upload_to='services/'),
            preserve_default=False,
        ),
    ]