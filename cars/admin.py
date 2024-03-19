from django.contrib import admin
from django.utils.html import format_html

from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" style="border-radius:20px;"/>'.format(obj.car_photo.url))

    thumbnail.short_description = 'car_photo'

    list_display = ("id", "thumbnail", "car_title", "city", "color", "model", "year", "body_style", "fuel_type", "is_featured")
    list_display_links = ("thumbnail", "car_title", "id")
    list_editable = ("is_featured",)
    search_fields = ("car_title", "id", "city", "model")
    list_filter = ("city", "model", "body_style", "fuel_type")

admin.site.register(Car, CarAdmin)