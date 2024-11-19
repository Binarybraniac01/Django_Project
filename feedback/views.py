from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from .models import *


def feedback(request):
    if request.method == "POST":
        data = request.POST

        mail = data.get("email")
        usermessage = data.get("message")
        rating = data.get("rating")

        Feedback.objects.create(
            user = request.user,
            email = mail,
            user_feedback = usermessage,
            rating = rating
        )

        # send feedback to website mail
        subject = f"This feedback is from {request.user}"
        message = usermessage
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['maharashtraforts.official@gmail.com']
        send_mail(subject, message, from_email, recipient_list)

        messages.info(request, "Feeedback submited successfully.")
        return redirect('/feedback/')

    return render(request, "feedback.html")
