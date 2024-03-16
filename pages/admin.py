from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" style="border-radius:50px;"/>'.format(obj.photo.url))

    thumbnail.short_description = 'photo'
    list_display = ("id", "thumbnail", "first_name", "designation", "created_date")
    list_display_links = ("id", "first_name", "thumbnail")
    list_filter = ("designation", "created_date")






admin.site.register(Team,TeamAdmin)