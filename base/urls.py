from rest_framework import routers

from base.api.user import UserCRUDView

router = routers.SimpleRouter()
router.register(r'users', UserCRUDView)

urlpatterns = [] + router.urls
