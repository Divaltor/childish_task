from django.db.models import Q, QuerySet
from django_filters import filters, FilterSet
from rest_framework import viewsets

from base.models import UserCar
from base.serializers.user_car import ReadOnlyUserCarSerializer, WriteOnlyUserCarSerializer

# noinspection PyMethodMayBeStatic
from shared.api.mixins import WriteOnlyModelViewSet


class UserCarFilterSet(FilterSet):
    user = filters.CharFilter(method='filter_user')
    order_by_odometer = filters.BooleanFilter(method='order_odometer')

    # I use this two filters instead DateRangeFilter because drf-yash show invalid value in swagger filters
    registration_date_before = filters.DateTimeFilter(field_name='first_reg', lookup_expr='lte')
    registration_date_after = filters.DateTimeFilter(field_name='first_reg', lookup_expr='gte')

    car = filters.CharFilter(method='filter_car')

    class Meta:
        model = UserCar
        fields = ['user', 'order_by_odometer', 'registration_date_before', 'registration_date_after', 'car']

    def filter_user(self, queryset: QuerySet[UserCar], name: str, value: str) -> QuerySet[UserCar]:
        return queryset.filter(
            Q(user__username__icontains=value)
            | Q(user__email__icontains=value)
            | Q(user__phone_number__icontains=value)
        )

    def order_odometer(self, queryset: QuerySet[UserCar], name: str, value: str) -> QuerySet[UserCar]:
        if value:
            return queryset.order_by('-odometer')

        return queryset

    def filter_car(self, queryset: QuerySet[UserCar], name: str, value: str) -> QuerySet[UserCar]:
        return queryset.filter(
            Q(car_model__name__icontains=value)
            | Q(car_model__car_brand__name__icontains=value)
        )


class ReadOnlyUserCarView(viewsets.ReadOnlyModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = ReadOnlyUserCarSerializer

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
            'car_model__updated_at',
            'car_model__car_brand__name'
        )


class WriteOnlyUserCarView(WriteOnlyModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = WriteOnlyUserCarSerializer
