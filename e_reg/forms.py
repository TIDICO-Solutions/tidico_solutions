from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from multiselectfield import MultiSelectField

from . import models


class GuestUserCreateForm(UserCreationForm):
    class Meta:
        fields = ("first_name", "last_name", "email", "password1", "password2")
        model = models.GuestUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["email"].label = "Email address"


class GuestUserUpdateForm(forms.ModelForm):
    class Meta:
        model = models.GuestUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'telephone_number',
            'address_street',
            'address_postcode',
            'address_city',
            'address_country',
        ]


class RoomPreferenceUpdateForm(forms.ModelForm):
    class Meta:
        model = models.GuestUser
        fields = [
            'room_preferences',
        ]
