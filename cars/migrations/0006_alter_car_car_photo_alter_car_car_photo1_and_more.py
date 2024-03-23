# Generated by Django 5.0.3 on 2024-03-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_car_photo_alter_car_car_photo1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(upload_to='photos/car/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo1',
            field=models.ImageField(blank=True, upload_to='photos/car/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo2',
            field=models.ImageField(blank=True, upload_to='photos/car/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo3',
            field=models.ImageField(blank=True, upload_to='photos/car/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo4',
            field=models.ImageField(blank=True, upload_to='photos/car/%y/%m/%d/'),
        ),
    ]
