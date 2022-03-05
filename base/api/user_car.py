from django.db.models import Q, QuerySet
from django_filters import filters, FilterSet
from rest_framework import viewsets

from base.models import UserCar
from base.serializers.user_car import UserCarSerializer


# noinspection PyMethodMayBeStatic
class UserCarFilterSet(FilterSet):
    user = filters.CharFilter(method='filter_user')
    biggest_run = filters.BooleanFilter(method='order_by_odometer')
    registration_date = filters.DateRangeFilter(field_name='first_reg')
    car = filters.CharFilter(method='filter_car')

    class Meta:
        model = UserCar
        fields = ['user', 'biggest_run', 'registration_date']

    def filter_user(self, queryset: QuerySet[UserCar], name: str, value: str) -> QuerySet[UserCar]:
        return queryset.filter(
            Q(user__username=value) | Q(user__email=value) | Q(user__phone_number=value)
        )

    def order_by_odometer(self, queryset: QuerySet[UserCar], name: str, value: str) -> QuerySet[UserCar]:
        if value:
            return queryset.order_by('-odometer')

        return queryset

    def filter_car(self, queryset: QuerySet[UserCar], name: str, value: str) -> QuerySet[UserCar]:
        return queryset.filter(
            Q(car_model__name=value) | Q(car_model__car_brand__name=value)
        )


class UserCarCRUDView(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer

    filterset_class = UserCarFilterSet

    def get_queryset(self) -> QuerySet[UserCar]:
        queryset = super().get_queryset()

        return queryset.select_related('user', 'car_model__car_brand').only(
            'user__phone_number',
            'user__deactivated_date',
            'user__email',
            'user__username',
            'user__first_name',
            'user__last_name',
            'user__is_active',
            'car_model__name',
            'car_model__updated_at'
        )
