# Generated by Django 5.1.2 on 2024-11-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0003_alter_all_recommendations_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_trips',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='all_recommendations',
            name='image_name',
            field=models.ImageField(blank=True, null=True, upload_to='img/recomendation_imgs'),
        ),
        migrations.AlterField(
            model_name='all_trips',
            name='forts_visited',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='all_trips',
            name='required_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='all_trips',
            name='trip_district',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]