from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from car_management.models import CarModel
from shared.models.mixins import CreatedTimeModel, SoftDeletableModel


class User(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    deactivated_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.is_active and self.deactivated_date is None:
            self.deactivated_date = timezone.now()

        if self.is_active:
            self.deactivated_date = None

        return super().save(*args, **kwargs)


class UserCar(SoftDeletableModel, CreatedTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    first_reg = models.DateTimeField(default=timezone.now)

    # Default 0 because user can buy auto right from shop
    # Float is used because odometer can contain meters in addition to the kilometers, for example
    odometer = models.FloatField(default=0)
