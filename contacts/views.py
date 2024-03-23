from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from contacts.models import Contact


# Create your views here.


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        email = request.POST['email']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            my_user_id = request.user.id
            has_contact = Contact.objects.filter(user_id=my_user_id, car_id=car_id)
            if has_contact:
                messages.error(request, 'You already have a inquiry on this car please wait')
                return redirect("/cars/" + car_id)

        contact = Contact(car_id=car_id, email=email, car_title=car_title
                          , user_id=user_id, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city, state=state, phone=phone, message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'new car inquiry',
            'you have new inquiry for the car' + car_title + 'please login to your admin panel for more detail',
            'ningoban@gmail.com',
            [admin_email],
            fail_silently=False
        )
        contact.save()
        messages.success(request, 'thank you for your request')

        return redirect("/cars/" + car_id)
    return render(request, "cars/car_detail.html")

