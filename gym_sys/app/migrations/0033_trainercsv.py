# Generated by Django 5.0.1 on 2024-02-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_trainersalary_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerCSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainercsv', models.FileField(null=True, upload_to='trainercsv/')),
            ],
        ),
    ]
