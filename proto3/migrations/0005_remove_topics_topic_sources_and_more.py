# Generated by Django 5.0.1 on 2024-02-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto3', '0004_remove_cttable_topics_ids_cttable_topics_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='Topic_Sources',
        ),
        migrations.RemoveField(
            model_name='trackeruser',
            name='Their_Login_map',
        ),
        migrations.AddField(
            model_name='cttable',
            name='Topic_Sources',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]