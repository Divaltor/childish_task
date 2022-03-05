from rest_framework import routers

from base.api.user import UserCRUDView
from base.api.user_car import UserCarCRUDView

router = routers.SimpleRouter()
router.register(r'users', UserCRUDView)
router.register(r'users-car', UserCarCRUDView)

urlpatterns = [] + router.urls
