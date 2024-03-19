from datetime import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from django.db import models
from djchoices import ChoiceItem, DjangoChoices

# Create your models here.

class Car(models.Model):
    state_choice = (
        ('TEHRAN', 'Tehran'),
        ('SHIRAZ', 'Shiraz'),
        ('HAMDAN', 'Hamedan'),
        ('ESFHAN', 'Esfehan'),
        ('KERMAN', 'Kerman'),
        ('ALBORZ', 'Alborz'),
        ('BANABS', 'Bandarabas'),
        ('RASHTG', 'Rashtgilan'),
        ('KORDTN', 'Kordestan'),
        ('GORGAN', 'Gorgan'),
        ('ZANJAN', 'Zanjan'),
        ('TABRIZ', 'Tabriz'),

    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = [
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    ]

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=100)
    state = models.CharField(max_length=6, choices=state_choice)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField("year", choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to="photos/%y/%m/%d/")
    car_photo1 = models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    car_photo2 = models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    car_photo3 = models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    car_photo4 = models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    features = MultiSelectField(choices=features_choices, max_length=200) #in django 5 yoy should delete some code in multiselectfield library to make this field work
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices,max_length=1)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    no_of_owner = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
