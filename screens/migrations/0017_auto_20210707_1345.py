# Generated by Django 3.2.3 on 2021-07-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0016_auto_20210616_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='ytid',
            field=models.CharField(blank=True, help_text='Only the YouTube Video ID is required. Only required if YouTube Type', max_length=20),
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(blank=True, help_text='Only required if website type', verbose_name='Website Address'),
        ),
    ]
