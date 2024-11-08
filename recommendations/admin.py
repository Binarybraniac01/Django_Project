from django.contrib import admin
from .models import *
from user.models import *


class all_trips_admin(admin.ModelAdmin):
    list_display = [
        "user",
        "trip_id",
        "trip_district",
        "forts_visited",
        "required_time",
        "minimum_cost",
        "date"
    ]
    # search_fields = ["name"]

    # def name(self, obj):
    #     name_obj =  UserData.objects.filter(user=obj.user).first()
    #     return name_obj.user


class all_recommendations_admin(admin.ModelAdmin):
    list_display = [
        "recommendation_id",
        "user",
        "recom_district",
        "recom_forts",
        "recom_title",
        "recom_details",
        "image_name",
        "date"
    ]
    

admin.site.register(all_trips, all_trips_admin)
admin.site.register(all_recommendations, all_recommendations_admin)