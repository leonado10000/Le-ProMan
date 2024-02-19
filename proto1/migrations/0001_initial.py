# Generated by Django 4.1.7 on 2024-01-31 13:32

from django.db import migrations, models
import proto1.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TrackerUser",
            fields=[
                (
                    "Their_ID",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("Their_Username", models.CharField(default="(^o^)", max_length=100)),
                ("Their_Name", models.CharField(max_length=100, null=True)),
                ("Their_Email", models.EmailField(max_length=254, null=True)),
                ("Their_Password", models.CharField(default="0000", max_length=20)),
                ("Their_Join_Date", models.DateTimeField(auto_now=True)),
                ("Their_last_login", models.DateTimeField(auto_now=True)),
                ("Their_Login_map", models.CharField(max_length=10000, null=True)),
                (
                    "Their_User_image",
                    models.CharField(default=proto1.models.def_img, max_length=150),
                ),
            ],
        ),
    ]
