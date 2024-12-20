import csv
from django.core.management.base import BaseCommand
from .models import *

class Command(BaseCommand):
    help = 'Import fort details from CSV file'

    def handle(self, *args, **kwargs):
        with open('home/fort_details.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                fort = Forts(
                    fort_district=row['district'],
                    fort_name=row['fort_name'],
                    fort_latitude=row['lat'],
                    fort_longitude=row['lon'],
                    link=row['link']
                )
                fort.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported fort details.'))


# This is for retriving accurate lat long data from forts.csv that i have downloaded 
def add_lat_lon():
    with open('home/forts.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                 fort = Forts.objects.filter(fort_name__icontains=row['name']).first()
                 if fort:
                    fort.fort_latitude = row['latitude']
                    fort.fort_longitude = row['longitude']
                    fort.save()
                    count += 1
                    print(f"Add lat long for {fort.fort_name}")
            print(count)


import os
def add_fort_images():
    count= 0
    for filename in os.listdir("public/media/img/fort_images"):
        # Get file name without extension and its extension
        base_name, ext = os.path.splitext(filename)
        
        # Search the fortname in fort_obj
        fort_obj = Forts.objects.filter(fort_name__icontains=base_name).first()
        if fort_obj:
            fort_obj.fort_image = f"img/fort_images/{filename}"
            fort_obj.save()
            count += 1
    print(count)
    