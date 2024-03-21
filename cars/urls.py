from django.urls import path
from . import views
from . import views
urlpatterns = [
    path("", views.cars, name="cars"),
    path('<id>', views.car_detail, name="car_detail"),
    path("search/", views.search, name="search"),


]