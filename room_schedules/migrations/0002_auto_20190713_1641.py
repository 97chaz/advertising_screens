# Generated by Django 2.2.1 on 2019-07-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(),
        ),
    ]
