from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path("services/", views.services, name='services'),

]