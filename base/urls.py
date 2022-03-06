from rest_framework import routers

from base.api.user import UserCRUDView
from base.api.user_car import ReadOnlyUserCarView, WriteOnlyUserCarView
from shared.api.mixins import ReadOnlyRouter

read_only_router = ReadOnlyRouter()
read_only_router.register(r'users-car', ReadOnlyUserCarView)

router = routers.SimpleRouter()
router.register(r'users', UserCRUDView)
router.register(r'users-car', WriteOnlyUserCarView)

urlpatterns = [] + router.urls + read_only_router.urls
