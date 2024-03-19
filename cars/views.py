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
    return render(request, "cars/cars.html", {"cars": page_car})


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    return render(request, "cars/car_detail.html", {"single_car": single_car})
