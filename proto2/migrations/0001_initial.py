# Generated by Django 4.1.7 on 2024-02-04 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "User_ID",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("Username", models.CharField(default="(^o^)", max_length=100)),
                ("Name", models.CharField(max_length=100, null=True)),
                ("Email", models.EmailField(max_length=254, null=True)),
                ("Password", models.CharField(default="0000", max_length=20)),
                ("Join_Date", models.DateTimeField(auto_now=True)),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("Login_map", models.CharField(max_length=10000, null=True)),
                ("User_image", models.CharField(default="def_img", max_length=150)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
