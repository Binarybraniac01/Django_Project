from django.db import models

# Create your models here.

class Fort_Details(models.Model):
    district = models.CharField(max_length=100)
    fort_name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    link = models.URLField()

    def __str__(self):
        return self.fort_name
