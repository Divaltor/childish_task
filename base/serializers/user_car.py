from rest_framework import serializers

from base.models import UserCar
from base.serializers.user import UserSerializer
from car_management.serializers.car_model import CarModelSerializer


class UserCarSerializer(serializers.ModelSerializer):

    car_model = CarModelSerializer()
    user = UserSerializer()

    class Meta:
        model = UserCar
        fields = [
            'car_model',
            'user',
            'first_reg',
            'odometer',
            'deleted_at',
            'created_at'
        ]
        read_only_fields = ['created_at', 'deleted_at']
