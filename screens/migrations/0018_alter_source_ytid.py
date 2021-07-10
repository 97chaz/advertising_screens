# Generated by Django 3.2.3 on 2021-07-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0017_auto_20210707_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='ytid',
            field=models.CharField(blank=True, help_text='Only the YouTube Video ID is required. Only required if YouTube Type', max_length=20, verbose_name='YouTube Video ID'),
        ),
    ]
