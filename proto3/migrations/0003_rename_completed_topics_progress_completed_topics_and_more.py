# Generated by Django 5.0.1 on 2024-02-12 09:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto3', '0002_remove_progress_completed_topic_ids_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='completed_topics',
            new_name='Completed_topics',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='incomplete_topics',
            new_name='Incomplete_topics',
        ),
        migrations.RemoveField(
            model_name='cttable',
            name='Related_topic_IDs',
        ),
        migrations.AlterField(
            model_name='cttable',
            name='Topics_IDs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
    ]
