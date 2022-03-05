from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from base.models import User


class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField(allow_null=True)
    phone = PhoneNumberField(source='phone_number')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'name',
            'is_active',
            'deactivated_date',
            'phone'
        ]
        read_only_fields = ['deactivated_date']

    # noinspection PyMethodMayBeStatic
    def get_name(self, obj: User) -> str | None:
        if obj.first_name and obj.last_name:
            return f'{obj.first_name} {obj.last_name}'

        if obj.first_name:
            return obj.first_name

        if obj.last_name:
            return obj.last_name

        return
