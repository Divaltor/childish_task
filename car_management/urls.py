from rest_framework import routers

from car_management.api.car_brand import CarBrandCRUDView
from car_management.api.car_model import CarModelCRUDView

router = routers.SimpleRouter()
router.register(r'car-brands', CarBrandCRUDView)
router.register(r'cars', CarModelCRUDView)


urlpatterns = [] + router.urls
