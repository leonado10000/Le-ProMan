# Generated by Django 5.0.1 on 2024-02-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto3', '0006_remove_cttable_course_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackeruser',
            name='Their_User_image',
            field=models.ImageField(default='default.jpg', upload_to='user_images/'),
        ),
    ]
