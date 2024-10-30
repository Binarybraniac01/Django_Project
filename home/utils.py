import csv
from django.core.management.base import BaseCommand
from .models import *

class Command(BaseCommand):
    help = 'Import fort details from CSV file'

    def handle(self, *args, **kwargs):
        with open('home/fort_details.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                fort = Fort_Details(
                    district=row['district'],
                    fort_name=row['fort_name'],
                    lat=row['lat'],
                    lon=row['lon'],
                    link=row['link']
                )
                fort.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported fort details.'))
