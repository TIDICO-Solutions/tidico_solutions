from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'first_name', 'last_name', "telephone_number", "address_street", "address_postcode", "address_city", "address_country", "room_preferences", "hotel_memberships"]

    list_display = ['email', 'id', 'first_name', 'last_name', 'is_superuser', "telephone_number", "address_street", "address_postcode", "address_city", "address_country"]


# Register your models here.
admin.site.register(models.GuestUser, UserAdmin)
admin.site.register(models.HotelProperty)
admin.site.register(models.User)
