# Generated by Django 5.0.3 on 2024-03-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=1),
        ),
    ]