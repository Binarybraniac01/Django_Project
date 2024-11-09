from django.shortcuts import render

from .models import *
from home.models import *

import random
from datetime import datetime

def ourplans(request):
    active2 = "active"

    planned_trips = all_trips.objects.filter(user=request.user).order_by('-trip_id')
    if not planned_trips:
        return render(request, "not_enough_data.html", context={"active2":active2})
    
    ############################ For Randomized Recommendations #########################################
    # check for the date constraints so that same day you dont make double recom for same user
    date_check = all_recommendations.objects.filter(user=request.user).first()
    if date_check is not None:
        first_date_obj = date_check.date
        current_date = datetime.now().date() # Convert the date string to a datetime object
        if first_date_obj != current_date:
            all_recommendations.objects.filter(user=request.user).delete()  
        else:
            print("dates Matched") 

    
    # Check if the date does not match with the current date the excute the code
    if date_check is None:
            # Retrieve unique trip districts using Django's ORM
            planned_trips_dist = list(
                all_trips.objects.filter(user=request.user)
                      .values_list('trip_district', flat=True)
                    .distinct()
            )
            print(planned_trips_dist)

            random_dist = random.sample(planned_trips_dist, min(5, len(planned_trips_dist)))
            recommend_dist_fort = []
            # Loop either 5 times or the number of unique districts, whichever is smaller
            for a in random_dist:
                f_names = []
                district_forts = Forts.objects.filter(fort_district= a)
                for b in district_forts:
                    f_names.append(b.fort_name)

                if f_names:
                    fort_names = random.sample(f_names, min(random.randint(4, 8), len(f_names)))

                    recommend_dist_fort.append((a, fort_names))
            
            print(recommend_dist_fort)

            n = 1
            for i in recommend_dist_fort:

                district = i[0]
                fort_names = i[1]
                title = f"Explore More of {i[0]}"
                details =(
                            f"Enjoy the historic beauties of {i[0]} district with personalised forts suggested for you. "
                            "Each fort holds tales of Maratha valor and offers breathtaking views, scenic drives, and a unique piece of history. "
                            "Perfect for adventurers and history lovers, this journey brings Maharashtra’s rich heritage to life with every stop. "
                        )
                recom_img = f"recom_{n}.jpg"
                n += 1 
                
                recommendation = all_recommendations.objects.create(
                    user = request.user,
                    recom_district = district,
                    recom_forts = fort_names,
                    recom_title = title,
                    recom_details = details,
                    image_name = recom_img
                )
                recommendation.save()

    tbl_data = all_recommendations.objects.filter(user=request.user)
    
    return render(request, "ourplans.html", context={"active2":active2, "planned_trips":planned_trips, "tbl_data":tbl_data})



def recommdirection(request):
    active2 = "active"

    # To show all recommendations in slider
    tbl_data = all_recommendations.objects.filter(user= request.user)

    # Code for after clicking get directions
    recom_id = request.POST.get('rec_id')
    print(recom_id)

    direc_data = all_recommendations.objects.filter(recommendation_id=recom_id).first()
    print(direc_data)

    # for checking in html page
    found = "found"

    # getting fort names and id
    fort_string = direc_data.recom_forts
    forts_list = eval(fort_string)
    print(forts_list)

    fortsname =[]

    for i in forts_list:
        get_data = Forts.objects.filter(fort_name=i).first()
        fortsname.append((get_data.fort_id, get_data.fort_name)) # todo: Unable to get fort id or any data

    return render(request, "ourplans.html", context= {"active2":active2, "tbl_data":tbl_data, "direc_data":direc_data, "found":found, "fortsname":fortsname})


# note : regarding recommendation generate plan
'''
- we have redirected the recommendation generate plan urls functionalities to home.views function
- The function will work for both home and recommendations as it delivers same functionalities
'''