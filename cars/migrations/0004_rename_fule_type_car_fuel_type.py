# Generated by Django 5.0.3 on 2024-03-17 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_doors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='fule_type',
            new_name='fuel_type',
        ),
    ]
