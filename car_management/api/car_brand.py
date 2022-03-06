from django.db.models import QuerySet
from django_filters import filters, FilterSet
from rest_framework import viewsets

from car_management.models import CarBrand
from car_management.serializers.car_brand import CarBrandSerializer


class CarBrandFilterSet(FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CarBrand
        fields = ['name']


class CarBrandCRUDView(viewsets.ModelViewSet):

    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

    filterset_class = CarBrandFilterSet

    def get_queryset(self) -> QuerySet[CarBrand]:
        queryset = super().get_queryset()

        return queryset.only('name')
