# Generated by Django 5.1.2 on 2024-11-07 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_recommendations',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='all_recommendations',
            name='trip_details',
        ),
        migrations.RemoveField(
            model_name='all_recommendations',
            name='trip_title',
        ),
        migrations.AddField(
            model_name='all_recommendations',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='all_recommendations',
            name='recom_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='all_recommendations',
            name='recom_district',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='all_recommendations',
            name='recom_forts',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='all_recommendations',
            name='recom_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='all_recommendations',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_recommendations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='all_recommendations',
            name='image_name',
            field=models.ImageField(upload_to='img/my_recommendations'),
        ),
        migrations.AlterField(
            model_name='all_trips',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]