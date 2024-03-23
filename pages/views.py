from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from cars.models import Car
from pages.models import Team


# Create your views here.


def home(request):
    teams = Team.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date').all()
    # search_field = Car.objects.values("model", "city", "body_style", "year")
    model_search = Car.objects.values_list("model", flat=True).distinct()
    city_search = Car.objects.values_list("city", flat=True).distinct()
    body_style_search = Car.objects.values_list("body_style", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    data = {
        "teams": teams,
        "featured_car": featured_car,
        "all_cars": all_cars,
        # "search_field": search_field
        "model_search": model_search,
        "body_style_search": body_style_search,
        "year_search": year_search,
        "city_search": city_search,
    }
    return render(request, "pages/index.html", data)


def services(request):
    return render(request, "pages/services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        message_body = "name :" + name + "email :" + email + "subject :" + subject + "phone :" + phone + "message :" + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            message_body,
            'you have new message from the site with this subject : ' + str(subject),
            'ningoban@gmail.com',
            [admin_email],
            fail_silently=False
        )
        messages.success(request, "Your message has been send")
        return redirect("contact")
    return render(request, "pages/contact.html")


def about_us(request):
    teams = Team.objects.all()
    data = {"teams": teams}
    return render(request, "pages/about_us.html",data)

