# Generated by Django 5.1.2 on 2024-11-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_delete_user_location_latitude_longitude_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='request_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
