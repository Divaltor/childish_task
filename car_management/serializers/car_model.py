from rest_framework import serializers

from car_management.models import CarModel
from car_management.serializers.car_brand import CarBrandSerializer


class CarModelSerializer(serializers.ModelSerializer):

    car_brand = CarBrandSerializer()

    class Meta:
        model = CarModel
        fields = ['id', 'name', 'car_brand', 'updated_at', 'created_at']
        read_only_fields = ['id', 'updated_at', 'created_at']
