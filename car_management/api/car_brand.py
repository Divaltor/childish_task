from django.db.models import QuerySet
from rest_framework import viewsets

from car_management.models import CarBrand
from car_management.serializers.car_brand import CarBrandSerializer


class CarBrandCRUDView(viewsets.ModelViewSet):

    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

    filterset_fields = ['name']

    def get_queryset(self) -> QuerySet[CarBrand]:
        queryset = super().get_queryset()

        return queryset.only('name')
