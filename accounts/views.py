from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from contacts.models import Contact


# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.check_password(password):
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login ')
            return redirect('login')

    return render(request,"accounts/login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username or email already exist")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Username or email already exists")
                    return redirect("register")
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    # user.save() #tis line i added here
                    # auth.login(request, user)
                    # messages.success(request, "you are now logged in")
                    # return redirect("dashboard")
                    user.save()
                    messages.success(request, "user create successfully")
                    return redirect("login")
        else:
            messages.error(request, "password must match")
            return redirect("register")
    return render(request,"accounts/signup.html")


@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by("created_date").filter(user_id=request.user.id)
    data = {
        "inquires": user_inquiry
    }
    return render(request, "accounts/dashboard.html", data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect("home")
    return render(request, "accounts/login.html")
