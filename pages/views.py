from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"pages/index.html")

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    return render(request, "pages/contact.html")

def about_us(request):
    return render(request, "pages/about_us.html")

