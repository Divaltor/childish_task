from django_filters import filters, FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_management.models import CarModel
from car_management.serializers.car_model import ReadOnlyCarModelSerializer, WriteOnlyCarModelSerializer
from shared.api.mixins import WriteOnlyModelViewSet


class CarModelFilterSet(FilterSet):

    brand = filters.CharFilter(field_name='car_brand__name', lookup_expr='icontains')
    search = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = CarModel
        fields = ['search', 'brand']


class ReadOnlyCarModelView(viewsets.ModelViewSet):

    queryset = CarModel.objects.all()
    serializer_class = ReadOnlyCarModelSerializer

    filterset_class = CarModelFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.select_related('car_brand')


class WriteOnlyCarModelView(WriteOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = WriteOnlyCarModelSerializer
