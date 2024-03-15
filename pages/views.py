from django.shortcuts import render

from pages.models import Team


# Create your views here.


def home(request):
    teams = Team.objects.all()
    data = {"teams": teams}
    return render(request, "pages/index.html", data)

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    return render(request, "pages/contact.html")

def about_us(request):
    teams = Team.objects.all()
    data = {"teams": teams}
    return render(request, "pages/about_us.html",data)

