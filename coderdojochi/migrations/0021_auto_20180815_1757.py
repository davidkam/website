# Generated by Django 2.0.6 on 2018-08-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0020_mentor_shirt_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='home_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='work_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
