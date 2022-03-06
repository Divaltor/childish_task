from rest_framework import serializers

from car_management.models import CarBrand


class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'deleted_at', 'created_at']
        read_only_fields = ['id', 'deleted_at', 'created_at']
        extra_kwargs = {
            'name': {'validators': []}
        }

    def create(self, validated_data: dict) -> CarBrand:
        car_brand, created = CarBrand.objects.get_or_create(
            name=validated_data.pop('name'),
            defaults=validated_data
        )

        return car_brand
