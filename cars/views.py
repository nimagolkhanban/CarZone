from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def cars(request):
    cars = Car.objects.order_by("-created_date")
    paginator = Paginator(cars,4)
    page = request.GET.get("page")
    page_car = paginator.get_page(page)
    model_search = Car.objects.values_list("model", flat=True).distinct()
    city_search = Car.objects.values_list("city", flat=True).distinct()
    body_style_search = Car.objects.values_list("body_style", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    data ={
        "cars": page_car,
        "model_search": model_search,
        "city_search": city_search,
        "body_style_search": body_style_search,
        "year_search":year_search,
    }
    return render(request, "cars/cars.html", data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    return render(request, "cars/car_detail.html", {"single_car": single_car})


def search(request):
    cars = Car.objects.order_by("-created_date")
    model_search = Car.objects.values_list("model", flat=True).distinct()
    city_search = Car.objects.values_list("city", flat=True).distinct()
    body_style_search = Car.objects.values_list("body_style", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    transmition_search = Car.objects.values_list("transmission", flat=True).distinct()

    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
           cars = cars.filter(description__icontains=keyword)

    if "model_car" in request.GET:
        model = request.GET["model_car"]
        if model:
            cars = cars.filter(model__iexact=model)

    if "year" in request.GET:
        year = request.GET["year"]
        if year:
            cars = cars.filter(description__iexact=year)

    if "body_style" in request.GET:
        body_style = request.GET["body_style"]
        if body_style:
            cars = cars.filter(description__iexact=body_style)

    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            cars = cars.filter(description__iexact=city)

    if "min_price" in request.GET:
        min_price = request.GET["min_price"]
        max_price = request.GET["max_price"]
        if max_price :
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    if "transmition" in request.GET:
        transmition = request.GET["transmition"]
        if transmition:
           cars = cars.filter(transmission__iexact=transmition)



    data ={
        "cars": cars,
        "model_search": model_search,
        "body_style_search": body_style_search,
        "year_search": year_search,
        "city_search": city_search,
        "transmition_search": transmition_search,


    }
    return render(request, "cars/search.html", data)