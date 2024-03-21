from django.shortcuts import render
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
    return render(request, "pages/contact.html")

def about_us(request):
    teams = Team.objects.all()
    data = {"teams": teams}
    return render(request, "pages/about_us.html",data)

