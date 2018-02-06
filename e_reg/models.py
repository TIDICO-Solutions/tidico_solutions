from django.conf import settings
from django.contrib.auth.models import (User, AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from multiselectfield import MultiSelectField

from .choices import COUNTRIES, ROOM_PREFERENCES

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

            user = self.model(email=self.normalize_email(email), username=username,)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(email, username, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(blank=True, null=True)
    telephone_number = models.CharField(max_length=20, default="")
    address_street = models.CharField(max_length=255, default="")
    address_postcode = models.CharField(max_length=10, default="")
    address_city = models.CharField(max_length=30, default="")
    address_country = models.CharField(max_length=500, choices=COUNTRIES)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    room_preferences = MultiSelectField(max_length=500, choices=ROOM_PREFERENCES, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def __str__(self):
        return "{}".format(self.first_name)

    def get_long_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('e_reg:my_profile')


class GuestUser(User):
    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('e_reg:my_profile')


class HotelProperty(models.Model):
    name = models.CharField(max_length=255)
    membership = models.CharField(max_length=30)
    room_features = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Hotel Properties"

    def __str__(self):
        return self.name
