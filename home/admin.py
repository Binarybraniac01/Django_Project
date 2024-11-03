from django.contrib import admin

# Register your models here.
from home.models import *

class Fort_Details_Admin(admin.ModelAdmin):
    list_display = ["fort_id","fort_district", "fort_name", "fort_latitude", "fort_longitude", "link"]
    search_fields = ["fort_district", "fort_name"]

admin.site.register(Forts, Fort_Details_Admin)
admin.site.register(latitude_longitude)
admin.site.register(user_location)
admin.site.register(Route)
admin.site.register(Result)
