from rest_framework import routers

from car_management.api.car_model import CarModelCRUDView

router = routers.SimpleRouter()
router.register(r'car-brands', CarModelCRUDView)


urlpatterns = [] + router.urls
