from django.db import models

from shared.models.mixins import CreatedTimeModel, SoftDeletableModel


class CarBrand(CreatedTimeModel, SoftDeletableModel):
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'car_brand'
        verbose_name = 'Car Brand'
        verbose_name_plural = 'Car Brands'

    def __str__(self) -> str:
        return self.name


class CarModel(CreatedTimeModel):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'car_model'
        verbose_name = 'Car Model'
        verbose_name_plural = 'Car Models'
        unique_together = [['name', 'car_brand']]

    def __str__(self) -> str:
        return f'{self.car_brand} - {self.name}'
