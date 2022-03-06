from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from base.models import User


class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField(allow_null=True)
    phone = PhoneNumberField(source='phone_number')
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'name',
            'is_active',
            'deactivated_date',
            'phone',
            'password'
        ]
        read_only_fields = ['id', 'deactivated_date']

    # noinspection PyMethodMayBeStatic
    def get_name(self, obj: User) -> str | None:
        if obj.first_name and obj.last_name:
            return f'{obj.first_name} {obj.last_name}'

        if obj.first_name:
            return obj.first_name

        if obj.last_name:
            return obj.last_name

        return

    def create(self, validated_data: dict) -> User:
        validated_data['password'] = make_password(validated_data.get('password'))
        
        return super().create(validated_data)
    
    def update(self, instance: User, validated_data: dict) -> dict:
        if password := validated_data.get('password'):
            validated_data['password'] = make_password(password)
       
        return super().update(instance, validated_data)
