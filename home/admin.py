from django.contrib import admin

# Register your models here.
from home.models import *

class Fort_Details_Admin(admin.ModelAdmin):
    list_display = ["district", "fort_name", "lat", "lon", "link"]
    search_fields = ["district", "fort_name"]

admin.site.register(Fort_Details, Fort_Details_Admin)
