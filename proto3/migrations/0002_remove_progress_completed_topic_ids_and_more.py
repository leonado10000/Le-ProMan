# Generated by Django 5.0.1 on 2024-02-12 09:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='Completed_topic_IDs',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='Incompleted_topic_IDs',
        ),
        migrations.AddField(
            model_name='progress',
            name='completed_topics',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='progress',
            name='incomplete_topics',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
    ]