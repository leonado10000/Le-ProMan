# Generated by Django 4.2.10 on 2024-02-17 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_courses_topics_rename_usr_profile_uname_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="uname",
            new_name="uid",
        ),
    ]
