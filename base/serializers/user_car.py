from rest_framework import serializers

from base.models import User, UserCar
from base.serializers.user import UserSerializer
from car_management.models import CarModel
from car_management.serializers.car_model import ReadOnlyCarModelSerializer


class ReadOnlyUserCarSerializer(serializers.ModelSerializer):

    car_model = ReadOnlyCarModelSerializer()
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
        read_only_fields = ['created_at', 'deleted_at', 'user', 'car_model']


class WriteOnlyUserCarSerializer(serializers.ModelSerializer):

    car_model = serializers.PrimaryKeyRelatedField(
        queryset=CarModel.objects.all()
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

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
