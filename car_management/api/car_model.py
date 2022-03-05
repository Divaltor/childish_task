from django_filters import filters, FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_management.models import CarModel
from car_management.serializers.car_model import CarModelSerializer


class CarModelFilterSet(FilterSet):

    brand = filters.CharFilter(field_name='brand__name', lookup_expr='contains')
    search = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = CarModel
        fields = ['search', 'brand']


class CarModelCRUDView(viewsets.ModelViewSet):

    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

    filterset_class = CarModelFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.select_related('brand')
