from rest_framework import routers

from car_management.api.car_brand import CarBrandCRUDView
from car_management.api.car_model import ReadOnlyCarModelView, WriteOnlyCarModelView
from shared.api.mixins import ReadOnlyRouter

read_only_router = ReadOnlyRouter()
read_only_router.register('cars', ReadOnlyCarModelView)


router = routers.SimpleRouter()
router.register(r'car-brands', CarBrandCRUDView)
router.register(r'cars', WriteOnlyCarModelView)


urlpatterns = [] + router.urls + read_only_router.urls
