from django.shortcuts import render
from home.models import *
from user.models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login-page/")
def home_view(request):

    active1 = "active"
    display = "none"
    found = "none"
    
    if request.method == "POST":
        print(request.method)
        
        data = request.POST
        # Get user district name from the submited form
        user_district = data.get('user_district')
        print(user_district)

        # Get district_name from database
        fortsname = Forts.objects.filter(fort_district=user_district)
        if fortsname:
            # declaring district name for later use
            # global district_name
            # district_name = user_district

            # adding district of current user
            if request.user.is_authenticated:
                user_data, created = UserData.objects.get_or_create(user=request.user)
                user_data.user_district = user_district
                user_data.save()

            # variable for showing container or simple text
            found = "found"
            display = "block"

            # Rendering Template if district name is found
            return render(request, "index.html", context = {"display":display, "active1":active1, "fortsname":fortsname,
                                   "found":found, "user_district":user_district})

        else:
            # if wrong district name is entered !!!
            print("District not found !!!")
            found = "nodata"
            return render(request, "index.html", context= {"display":display, "active1":active1, "found":found})


    # This will load the index file at start , when no entry is entered
    return render(request, "index.html", context= {"display":display, "active1":active1, "found":found})



# @login_required(login_url="/login-page/")
def send_coordinates(request):
    if request.method == "POST":

        usr_latitude = request.POST.get("latitude")
        usr_longitude = request.POST.get("longitude")
        print(usr_latitude)
        print(usr_longitude)

        # deleting database data if already existed
        latitude_longitude.objects.all().delete()

        # Inserting user location to database
        user_lat_long = latitude_longitude.objects.create(origin_latitude=usr_latitude, origin_longitude=usr_longitude)
        user_lat_long.save()
        print("Co-ordinated recieved")

        # Deleting user locations table
        user_location.objects.all().delete()
        

        new_user_lat_long = user_location.objects.create(user_latitude=usr_latitude, user_longitude=usr_longitude)
        new_user_lat_long.save()

        # adding data in Userdata table
        if request.user.is_authenticated:
            user_data = UserData.objects.get(user=request.user)
            user_data.curr_lat = usr_latitude
            user_data.curr_log = usr_longitude
            user_data.save()

        # deleting route table data
        Route.objects.all().delete()
        print("deleted route table vales ")

        # deleting result table data
        Result.objects.all().delete()
        print("deleted result table vales ")

        data = {"success_msg": "Coordinates recieved successfully!"} # json response need data argument for the our data to load

        return JsonResponse(data= data, safe=False) # safe to be false is need for django to serialize the data 

