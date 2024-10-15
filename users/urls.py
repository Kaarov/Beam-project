from rest_framework import routers

from .views import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(
    "user", viewset=UserViewSet, basename="user"
)
router.register(
    "profile", viewset=ProfileViewSet, basename="profile"
)

urlpatterns = []

urlpatterns += router.urls
