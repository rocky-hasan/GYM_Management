# Generated by Django 5.0.1 on 2024-01-30 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_subscription_regis_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name_plural': 'Banners'},
        ),
        migrations.CreateModel(
            name='TrainerAchivements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='achivements/')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.trainer')),
            ],
        ),
    ]