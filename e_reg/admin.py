from django.contrib import admin

from . import models

class HotelMembershipInline(admin.StackedInline):
    model = models.HotelMembership


class UserAdmin(admin.ModelAdmin):
    inlines = [HotelMembershipInline,]

    fields = ['email', 'first_name', 'last_name', "telephone_number", "address_street", "address_postcode", "address_city", "address_country", "room_preferences"]

    list_display = ['email', 'id', 'first_name', 'last_name', 'is_superuser', "telephone_number", "address_street", "address_postcode", "address_city", "address_country"]


class HotelMembershipAdmin(admin.ModelAdmin):
    list_display = ["guestuser", "membership_programme_name", "membership_number"]


# Register your models here.
admin.site.register(models.GuestUser, UserAdmin)
admin.site.register(models.HotelProperty)
admin.site.register(models.User)
admin.site.register(models.HotelMembership, HotelMembershipAdmin)
