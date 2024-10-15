from rest_framework import routers

from .views import ProductViewSet, PurchaseViewSet

router = routers.DefaultRouter()
router.register(
    "product", viewset=ProductViewSet, basename="product"
)
router.register(
    "purchase", viewset=PurchaseViewSet, basename="purchase"
)

urlpatterns = []

urlpatterns += router.urls
