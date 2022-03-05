from rest_framework import serializers

from car_management.models import CarBrand


class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'deleted_at', 'created_at']
        read_only_fields = ['id', 'deleted_at', 'created_at']
